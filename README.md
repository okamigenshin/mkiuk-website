# Martin Kaye Interiors website

This is the static Martin Kaye Interiors website, published at https://okamigenshin.github.io/mkiuk-website/. To preview it locally, run `python -m http.server 8765` in this folder and visit `http://localhost:8765/`.

## Source and limits

- Rebuilt from the Wayback Machine capture of the homepage on 12 July 2025, with About, Contact and Blog captures from the same day.
- The original MKI logo, composite project image, and showroom photograph were recovered from archived files. The layout and main colours follow the captured website. The copy has since been edited for clarity and search previews.
- The archive did not preserve the homepage hero file or department card photographs. The hero uses a Wix photograph with the same source image identifier as the missing WordPress hero, but an exact match to that version cannot be verified. Department cards still use colour backgrounds.
- Contact now gives visitors a clear way to enquire, and About explains the showroom, measuring, making and fitting process. The Blog archive was empty, so the local Journal page is marked `noindex` and omitted from navigation.
- The Portfolio and Book Online links in the archive redirected to Google sign-in and no public page content could be recovered. The local Portfolio page is marked `noindex` until fuller project material is available. The visit page offers phone and email contact and does not claim to provide live booking.
- The archived social icons and policy labels did not expose confirmed destinations, so they were removed rather than shown as dead links.

## Hosting

GitHub Pages publishes the `main` branch from the repository root. The site uses relative paths, so it works at the repository Pages URL and at a future custom domain. `.nojekyll` is included. The custom domain is not configured yet.

The `.recovery` folder and `AUDIT.md` are local working records and are excluded from Git.
