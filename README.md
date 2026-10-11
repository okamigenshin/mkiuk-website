# Martin Kaye Interiors website

This is the static Martin Kaye Interiors website, published at https://mkiuk.com/. To preview it locally, run `python -m http.server 8765` in this folder and visit `http://localhost:8765/`.

## Source and limits

- Rebuilt from the Wayback Machine capture of the homepage on 12 July 2025, with About, Contact and Blog captures from the same day.
- The original MKI logo, composite project image, and showroom photograph were recovered from archived files. The layout and main colours follow the captured website. The copy has since been edited for clarity and search previews. Dedicated service pages, FAQs, brand enquiries, verified showroom details and search metadata were added on 11 October 2026. See [SEO-IMPLEMENTATION.md](SEO-IMPLEMENTATION.md) for sources and remaining case-study/profile work.
- The archive did not preserve the homepage hero file or department card photographs. The hero uses a Wix photograph with the same source image identifier as the missing WordPress hero, but an exact match to that version cannot be verified. Department cards still use colour backgrounds.
- Contact gives visitors phone and email paths and a local enquiry brief that prepares a draft in their own email app. It does not submit or send an enquiry. About explains the showroom, measuring, making and fitting process. The Blog archive was empty, so the local Journal page is marked `noindex` and omitted from navigation.
- The Portfolio and Book Online links in the archive redirected to Google sign-in and no public page content could be recovered. The local Portfolio page is marked `noindex` until fuller project material is available. The visit page offers phone and email contact and does not claim to provide live booking.
- The archived social icons and policy labels did not expose confirmed destinations, so they were removed rather than shown as dead links.

## Hosting

GitHub Pages publishes an explicitly packaged website artifact from `main`, after the Site safety workflow passes. Pull requests run the checks with read-only permissions and cannot deploy. Only the deployment job receives Pages and OIDC write permissions. The custom domain is `mkiuk.com`, with HTTPS enforced. `.nojekyll` is included.

Run `python .github/scripts/check_site.py` before submitting changes. See [SECURITY.md](SECURITY.md) for the security controls and remaining hosting limits.

## Local search implementation

The site has 16 HTML pages, including dedicated made-to-measure blinds and Luxaflex dealer pages, a privacy notice and a branded 404. The sitemap contains the 12 indexable pages; Portfolio, Journal, Privacy and 404 retain noindex. Service pages use the shared 1280px container, existing MKI logo, visual introductions and clear enquiry paths. Illustrations explain window-treatment options without claiming to show completed MKI projects. The curtain photograph is style inspiration; the showroom photograph is recovered MKI material.

Five manufacturer logos are original assets retrieved from official brand sites. Designers Guild and Somfy remain named links because their official marks could not be retrieved reliably. See [ASSET-SOURCES.md](ASSET-SOURCES.md) for provenance and relationship wording.

Google Business Profile management, approved project photographs and customer records remain owner-dependent. The ignored `.recovery/implementation/` folder contains blank lead and project templates and a historical HTML URL inventory for review. None of those operational files is published.

The `.recovery` folder and `AUDIT.md` are local working records and are excluded from Git.
