"""Check the public static site using only the Python standard library."""

from html.parser import HTMLParser
from pathlib import Path
import base64
import hashlib
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from urllib.parse import parse_qs, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
DOMAIN = "https://mkiuk.com"
ROUTES = (
    "", "about-us", "portfolio", "contact", "blog", "book-online",
    "services", "bespoke-curtains", "shutters", "motorised-blinds", "faq",
    "brands-and-partners",
)
PAGES = [ROOT / route / "index.html" if route else ROOT / "index.html" for route in ROUTES]
ERRORS = []


def error(path, message):
    label = path.relative_to(ROOT) if isinstance(path, Path) else path
    ERRORS.append(f"{label}: {message}")


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.csp = None
        self.referrer = None
        self.title = []
        self.in_title = False
        self.description = None
        self.robots = ""
        self.canonical = None
        self.h1_count = 0
        self.images = 0
        self.jsonld = []
        self.current_script = None
        self.current_iframe = None

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if any(name.lower().startswith("on") for name in attrs):
            error(self.path, "inline event handler")
        if tag == "base":
            error(self.path, "base element is forbidden")
        if tag == "h1":
            self.h1_count += 1
        if tag == "img":
            self.images += 1
            if "alt" not in attrs:
                error(self.path, "image is missing alt text")
            for dimension in ("width", "height"):
                if not re.fullmatch(r"[1-9][0-9]*", attrs.get(dimension, "")):
                    error(self.path, f"image is missing a positive {dimension}")
        if tag == "script":
            self.current_script = {"attrs": attrs, "body": []}
        if tag == "iframe":
            self.current_iframe = attrs
            self.validate_iframe(attrs.get("src", ""))
        if tag == "title":
            self.in_title = True
        if tag == "meta":
            if attrs.get("http-equiv", "").lower() == "content-security-policy":
                if self.csp is not None:
                    error(self.path, "duplicate Content-Security-Policy")
                self.csp = attrs.get("content", "")
            if attrs.get("name", "").lower() == "referrer":
                self.referrer = attrs.get("content")
            if attrs.get("name", "").lower() == "description":
                if self.description is not None:
                    error(self.path, "duplicate meta description")
                self.description = attrs.get("content", "").strip()
            if attrs.get("name", "").lower() == "robots":
                self.robots = attrs.get("content", "").lower()
        if tag == "link" and "canonical" in attrs.get("rel", "").lower().split():
            if self.canonical is not None:
                error(self.path, "duplicate canonical link")
            self.canonical = attrs.get("href")
        for name in ("href", "src"):
            value = attrs.get(name, "")
            if not value:
                continue
            url = urlsplit(value)
            if url.scheme.lower() in ("javascript", "data", "http") or value.startswith("//"):
                error(self.path, f"unsafe resource URL {value}")
            if not url.scheme and not url.netloc and url.path:
                target = (ROOT / unquote(url.path.lstrip("/")) if url.path.startswith("/")
                          else self.path.parent / unquote(url.path)).resolve()
                if not target.is_relative_to(ROOT) or not target.exists():
                    error(self.path, f"missing/outside link {value}")

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)
        if self.current_script is not None:
            self.current_script["body"].append(data)

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "script" and self.current_script is not None:
            self.validate_script(self.current_script)
            self.current_script = None
        if tag == "iframe":
            self.current_iframe = None

    def validate_script(self, script):
        attrs = script["attrs"]
        if attrs.get("src"):
            src = urlsplit(attrs["src"])
            if src.scheme or src.netloc or attrs["src"].startswith("//"):
                error(self.path, "scripts must be same-origin only")
            if script["body"] and "".join(script["body"]).strip():
                error(self.path, "external script must not contain inline code")
            return
        if attrs.get("type", "").lower().strip() != "application/ld+json":
            error(self.path, "inline executable scripts are forbidden")
            return
        body = "".join(script["body"])
        try:
            data = json.loads(body)
        except (json.JSONDecodeError, TypeError):
            error(self.path, "JSON-LD script must contain valid JSON")
            return
        if (not isinstance(data, dict) or data.get("@context") != "https://schema.org"
                or not isinstance(data.get("@graph"), list) or not data["@graph"]
                or not all(isinstance(node, dict) for node in data["@graph"])):
            error(self.path, "JSON-LD must be an object with schema.org @context and @graph")
            return
        digest = base64.b64encode(hashlib.sha256(body.encode("utf-8")).digest()).decode("ascii")
        self.jsonld.append("'sha256-" + digest + "'")

    def validate_iframe(self, value):
        if self.path.parent.name != "contact":
            error(self.path, "iframes are allowed only on the contact page")
            return
        url = urlsplit(value)
        query = parse_qs(url.query, keep_blank_values=True)
        if (url.scheme != "https" or url.hostname != "www.google.com" or url.port is not None
                or url.username is not None or url.password is not None or url.path != "/maps"
                or url.fragment or set(query) != {"q", "output"}
                or len(query.get("q", [])) != 1 or not query["q"][0].strip()
                or query.get("output") != ["embed"]):
            error(self.path, "map iframe must use https://www.google.com/maps?q=...&output=embed")


def csp_directives(page):
    directives = {}
    for item in (page.csp or "").split(";"):
        values = item.strip().split()
        if values:
            key = values[0].lower()
            if key in directives:
                error(page.path, f"duplicate CSP directive {key}")
            directives[key] = values[1:]
    return directives


tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
for name in filter(None, tracked):
    parts = Path(name).parts
    if any(part == ".env" or part.startswith(".env.") for part in parts) or re.search(
        r"\.(?:pem|key|pfx|p12|sqlite|sqlite3|db|sql|bak)$", name, re.I
    ) or any(part in (".recovery", "node_modules", "__pycache__") for part in parts):
        error(name, "private/generated file must not be committed")

titles = {}
descriptions = {}
indexable = set()
for path, route in zip(PAGES, ROUTES):
    if not path.is_file():
        error(path, "expected route page is missing")
        continue
    page = Page(path)
    page.feed(path.read_text(encoding="utf-8"))
    page.close()
    title = "".join(page.title).strip()
    description = page.description or ""
    if not title:
        error(path, "missing page title")
    elif title in titles:
        error(path, f"title duplicates {titles[title]}")
    else:
        titles[title] = route or "/"
    if not description:
        error(path, "missing meta description")
    elif description in descriptions:
        error(path, f"meta description duplicates {descriptions[description]}")
    else:
        descriptions[description] = route or "/"
    if page.h1_count != 1:
        error(path, f"expected exactly one h1, found {page.h1_count}")
    expected_url = DOMAIN + (f"/{route}/" if route else "/")
    if page.canonical != expected_url:
        error(path, f"canonical must be {expected_url}")
    if "noindex" not in page.robots:
        indexable.add(expected_url)
    directives = csp_directives(page)
    for directive in ("default-src", "object-src", "base-uri", "form-action"):
        if directives.get(directive) != ["'none'"]:
            error(path, f"{directive} must deny by default")
    expected_script = ["'self'"] + sorted(page.jsonld)
    if directives.get("script-src") != expected_script:
        error(path, "script-src must contain only 'self' and exact hashes for valid JSON-LD")
    expected_frame = ["https://www.google.com"] if route == "contact" else None
    if directives.get("frame-src") != expected_frame:
        error(path, "frame-src must allow only the approved contact map and be absent elsewhere")
    if any(value in ("'unsafe-inline'", "'unsafe-eval'") for values in directives.values() for value in values):
        error(path, "unsafe CSP exception")
    if page.referrer != "no-referrer":
        error(path, "missing referrer policy")

if (ROOT / "CNAME").read_text(encoding="utf-8").strip() != "mkiuk.com":
    ERRORS.append("Unexpected publishing domain")

sitemap_path = ROOT / "sitemap.xml"
try:
    sitemap = ET.parse(sitemap_path).getroot()
    namespace = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
    sitemap_urls = [node.text.strip() for node in sitemap.findall(f"{namespace}url/{namespace}loc")
                    if node.text]
    if sitemap.tag != namespace + "urlset":
        ERRORS.append("sitemap.xml: expected a standard sitemap urlset")
    if len(sitemap_urls) != len(set(sitemap_urls)):
        ERRORS.append("sitemap.xml: duplicate URLs")
    if set(sitemap_urls) != indexable:
        ERRORS.append("sitemap.xml: URLs must exactly match canonical indexable pages")
except (OSError, ET.ParseError) as exc:
    ERRORS.append(f"sitemap.xml: missing or invalid XML ({exc})")

if ERRORS:
    raise SystemExit("\n".join(ERRORS))
print(f"Site safety passed: {len(PAGES)} pages and {len(list(filter(None, tracked)))} tracked files.")
