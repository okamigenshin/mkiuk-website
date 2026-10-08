"""Check files intended for this static public site, without third-party packages."""

from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
PAGES = [ROOT / "index.html"] + [ROOT / route / "index.html" for route in
    ("about-us", "portfolio", "contact", "blog", "book-online")]
errors = []


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.csp = None
        self.referrer = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if any(name.lower().startswith("on") for name in attrs):
            errors.append(f"{self.path.relative_to(ROOT)}: inline event handler")
        if tag == "base":
            errors.append(f"{self.path.relative_to(ROOT)}: base element is forbidden")
        if tag == "script" and (not attrs.get("src") or urlsplit(attrs["src"]).scheme
                                or attrs["src"].startswith("//")):
            errors.append(f"{self.path.relative_to(ROOT)}: script must be a local file")
        if tag == "meta":
            if attrs.get("http-equiv", "").lower() == "content-security-policy":
                self.csp = attrs.get("content", "")
            if attrs.get("name") == "referrer":
                self.referrer = attrs.get("content")
        for name in ("href", "src"):
            value = attrs.get(name, "")
            url = urlsplit(value)
            if url.scheme.lower() in ("javascript", "data", "http") or value.startswith("//"):
                errors.append(f"{self.path.relative_to(ROOT)}: unsafe resource URL")
            if not value or url.scheme or url.netloc or not url.path:
                continue
            target = ROOT / unquote(url.path.lstrip("/")) if url.path.startswith("/") else self.path.parent / unquote(url.path)
            target = target.resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f"{self.path.relative_to(ROOT)}: missing/outside link {value}")


tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode().split("\0")
for name in filter(None, tracked):
    parts = Path(name).parts
    if any(part == ".env" or part.startswith(".env.") for part in parts) or re.search(
        r"\.(?:pem|key|pfx|p12|sqlite|sqlite3|db|sql|bak)$", name, re.I
    ) or any(part in (".recovery", "node_modules", "__pycache__") for part in parts):
        errors.append(f"{name}: private/generated file must not be committed")

for path in PAGES:
    page = Page(path)
    page.feed(path.read_text(encoding="utf-8"))
    directives = {}
    for item in (page.csp or "").split(";"):
        values = item.strip().split()
        if values:
            directives[values[0]] = values[1:]
    for directive in ("default-src", "object-src", "base-uri", "form-action"):
        if directives.get(directive) != ["'none'"]:
            errors.append(f"{path.relative_to(ROOT)}: {directive} must deny by default")
    if directives.get("script-src") != ["'self'"]:
        errors.append(f"{path.relative_to(ROOT)}: scripts must be same-origin only")
    if "'unsafe-inline'" in (page.csp or "") or "'unsafe-eval'" in (page.csp or ""):
        errors.append(f"{path.relative_to(ROOT)}: unsafe CSP exception")
    if page.referrer != "no-referrer":
        errors.append(f"{path.relative_to(ROOT)}: missing referrer policy")

if (ROOT / "CNAME").read_text(encoding="utf-8").strip() != "mkiuk.com":
    errors.append("Unexpected publishing domain")

if errors:
    raise SystemExit("\n".join(errors))
print(f"Site safety passed: {len(PAGES)} pages and {len(list(filter(None, tracked)))} tracked files.")
