# SEO, AEO and GEO implementation handoff

Checked 11 October 2026. This is the evidence and pending-work checklist for the local MKI site. It records confirmed facts and primary sources; it does not claim search visibility or an unverified supplier relationship.

## Confirmed identity and claims

- The live [Luxaflex dealer listing for Martin Kaye Interiors](https://www.luxaflex.co.uk/find-showroom/martin-kaye-interiors-mill-hill/appointment/) confirms the showroom name, `625 Watford Way, Mill Hill, NW7 3JN`, telephone `0208 906 9900`, dealer status, and listed Luxaflex products. The page gives weekday hours as 08:30–17:30 and weekends closed. Treat these as the current public showroom details unless the business confirms otherwise.
- [Companies House](https://find-and-update.company-information.service.gov.uk/company/03079233) lists the active legal entity as **MARTIN KAYE INTERIORS LIMITED**, company number 03079233, with registered office `625 Watford Way, London, NW7 3JN`. It also lists SIC 47510, retail sale of textiles in specialised stores. Keep legal entity wording distinct from the customer-facing showroom name, and do not silently replace “Mill Hill” with “London” across public listings.
- Recovered July 2025 site content supports the existing core service scope: bespoke curtains, blinds and shutters. The archive source used for recovery is [Wayback snapshot](https://web.archive.org/web/20250712085437id_/http://www.mkiuk.com/). New claims about specific installations, materials, projects, or outcomes need current first-party evidence.
- Portfolio evidence currently consists of a composite image showing a retail shopfront and patterned curtains/sheers. It does not establish the fabric brand, customer identity, fabric type, installation, or outcome. Keep portfolio content out of search indexing until case-study details are confirmed and approved.
- Luxaflex is the only verified dealer relationship in this handoff. The following manufacturer pages confirm their product categories only; they do **not** prove MKI has an account, dealership, stock, or permission to use partner logos: Romo [fabrics and wallcoverings](https://www.romo.com/); Sanderson [fabrics, wallpaper and paint](https://www.sanderson.design/); Designers Guild [fabric and wallpaper collections](https://www.designersguild.com/en-gb/new-fabrics-wallpapers/l1299); Colefax and Fowler [fabrics and wallpapers](https://www.colefax.com/); Silent Gliss [motorised curtains, blinds and other shading](https://www.silentgliss.co.uk/engb/smart-motorisation/motorisation/); Somfy [motorised blinds and curtain tracks](https://www.somfy.co.uk/products/discover-our-smart-applications/blinds-and-curtains).

## Search guidance confirmed

- Google says there is no special schema markup required for generative-AI search features; useful original content and established Search fundamentals remain central. See [Google's generative AI search guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).
- Google retired FAQ rich results from Search starting 7 May 2026. Keep an `/faq/` page if it helps customers, but do not promise FAQ rich-result eligibility or add FAQ markup for that purpose. See [Google Search documentation updates](https://developers.google.com/search/updates).
- Use structured data only to accurately describe visible page content. Google's [LocalBusiness structured-data guide](https://developers.google.com/search/docs/appearance/structured-data/local-business) is relevant for the showroom page. Build and reference a sitemap according to [Google's sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap); use robots.txt for crawl access, not as a way to remove URLs from the index ([robots.txt guide](https://developers.google.com/search/docs/crawling-indexing/robots/intro)).
- No rankings, rich results, AI citations, or traffic gains can be guaranteed by these changes.

## Completed locally

- Added a services hub and dedicated pages for bespoke curtains, shutters and motorised blinds, with practical material, fitting and control guidance.
- Added visible FAQs and a brands page. Luxaflex is identified as a verified dealer relationship. At Hemanth's direction, Romo, Sanderson, Designers Guild, Colefax and Fowler, Silent Gliss and Somfy are named as brands to discuss, with availability confirmed during enquiry. No other dealership or partnership claim is made.
- Added matching canonical URLs, social previews, business/WebSite/WebPage JSON-LD, and Service/BreadcrumbList markup on the three landing pages. The showroom address is repeated consistently in the footer, Contact, visit page and business schema.
- Added a lazy-loaded Google map on Contact and direct directions links.
- Converted the portfolio composite from 391,604 bytes to 43,694-byte WebP (89% smaller), and the hero from 93,266 to 26,668 bytes (71% smaller). Added factual alt text and a portfolio caption.
- Added robots.txt and a sitemap with the ten indexable pages. Portfolio and the empty Journal retain noindex.
- Updated the safety checker and explicit GitHub Pages packaging list for all 12 routes. Production publication uses the existing protected-main GitHub Pages workflow.

## Remaining content and external work

- [ ] Obtain approved individual project photographs and descriptions: window type, fabric/product, hardware, installation solution and outcome. Write case studies from those records, then reconsider Portfolio indexing.
- [ ] Google Maps core identity checked. The confirmed 08:30–17:30 weekday hours were submitted as a public correction on 11 October; Google review remains pending. Obtain the exact Houzz profile URL and existing Business Profile owner's access route.
- [ ] Confirm current sample/ordering access and any specific authorised-dealer wording for non-Luxaflex brands before adding stronger relationship claims or brand logos.
- [ ] Confirm survey/fitting coverage, prices, guarantees and lead times before adding specific promises. Weekday opening hours are confirmed and published; additional served areas are not claimed.
- [ ] Inspect indexing and search performance when Search Console processing finishes. The previous sitemap submission succeeded with ten pages discovered; the new release adds two indexable service URLs. Local checks do not verify ranking or traffic improvements.

## Local validation and design

- Site safety checks pass for all 12 routes, including structured-data hashes, local links, unique metadata and sitemap/indexability consistency.
- Browser checks found no horizontal overflow, broken images or header overlap at mobile and desktop sizes. Exact 390px mobile emulation was checked on every route.
- Shared Jost headings, Poppins body text, gold/ink/surface tokens, page-title sizing, buttons, navigation and footer are reused. Services remains highlighted on its detail pages.
- Mobile menu open/close and FAQ expansion were verified. The Google Maps embed loaded successfully and visually located Martin Kaye Interiors.
- The local preview is available at http://127.0.0.1:8765/services/. Production is served at https://mkiuk.com/ through GitHub Pages; a successful workflow and live checks establish release status.

## Source notes

Brand facts were checked on each manufacturer's official site. Category summaries above are deliberately limited to what those pages describe. The current live Google Search documentation was checked on 11 October 2026; its guidance can change, so recheck at implementation and before any later SEO claim.


## Follow-up checks on 11 October 2026

- Corrected all six new page containers to the same 1280px maximum as About and Contact. Verified matching left alignment and widths on desktop and mobile, with no overflow.
- Added the Companies House number visibly to every footer and linked the business graph to the official register, Luxaflex dealer record and exact Google Maps profile.
- Changed the existing curtain hero from a CSS-only background to a normal high-priority image with a factual alt description, preserving its appearance. Added image entries and the actual update date to the sitemap.
- Recovered MKI's own historical featured-project titles from the 2024 site archive: Gucci London, Hermès Sloane Street and Everyman at Selfridges. Added the titles to Portfolio. Full material/installation case studies and individual approved photographs remain unavailable; Portfolio retains noindex.
- The public Google Maps profile matches the trading name, 625 Watford Way / NW7 3JN, telephone and website. Google abbreviates Way as Wy and omits Mill Hill; these identify the same address and are not evidence of a location mismatch. Google listed weekday hours 09:00–17:00; Hemanth subsequently confirmed 08:30–17:30 and a correction was submitted for review.
- The exact Google profile was checked through https://www.google.com/maps/search/?api=1&query=Martin+Kaye+Interiors+625+Watford+Way+London+NW7+3JN . The hours correction was submitted through Maps, but no managed Business Profile fields were edited. Focused searches found no verified Houzz profile; an exact URL is still needed.
- Search Console automatically verified the https://mkiuk.com/ URL-prefix property using the existing domain-provider verification. No new DNS record or verification file was added. Its indexing/performance reports are processing.
- The sitemap submission was accepted, but the initial report showed Couldn't fetch. Live HTTP checks return valid application/xml with HTTP 200. Google's live test of /services/ confirms URL is available to Google and Page can be indexed. Final processing status and indexing request results are recorded below when verified.


## Confirmed opening hours

Hemanth confirmed on 11 October 2026 that weekday opening hours are 08:30–17:30. These hours are now visible on Contact, Arrange a Visit, FAQ and every footer, and repeated in each business openingHoursSpecification. This matches the Luxaflex listing. External Google profile update status is recorded in the local verification log.

## Search Console follow-up result

On 11 October 2026 Google successfully read sitemap.xml and discovered all 10 indexable pages. The /services/ live test passed and its indexing request was accepted into the priority crawl queue. These are discovery/request confirmations, not proof of completed indexing or ranking. Screenshots and the release verification record are retained in the ignored .recovery folder.

## Homeowner strategy implementation

Hemanth prioritised local homeowners around Mill Hill before trade clients. The implementation adds dedicated `/blinds/` and `/luxaflex-blinds/` pages, with useful styles, light/privacy guidance, fitting information and FAQs. The Luxaflex product descriptions are based on its official dealer and product pages; availability and exact options remain enquiry-specific.

The homepage now gives the four core homeowner services clear visual links. Service introductions pair concise copy with the recovered showroom photograph, curtain style inspiration or labelled explanatory illustrations. All public page containers share the same maximum width. The original MKI logo remains in the header and footer. Five original manufacturer marks were retrieved from official sites; the brands page preserves the distinction between a verified Luxaflex dealership and brands to discuss. See ASSET-SOURCES.md.

Contact has a client-side enquiry brief that validates the service and project fields, prepares an encoded email draft and previews it as plain text. It neither uploads nor sends data and has no persistent storage or analytics. Visitors choose whether to open their email app and send. Phone/email paths remain usable without JavaScript. A factual privacy notice and a root-path branded 404 are included; both are noindex and omitted from the sitemap.

The safety checker covers all sixteen HTML pages, exact schema hashes, explicit indexability and safe SVG content. The protected-main deployment allowlist includes the three new directories and 404. The sitemap now has twelve indexable URLs. Browser checks at 390px and 1024px found no horizontal overflow; the enquiry helper's required fields, encoded body, safe plain-text preview and stale-draft reset were verified. Desktop visual checks cover the new service and brand layouts. No email was sent during testing.

The www HTTPS test failed certificate hostname verification while the apex remained available. GitHub Pages reported certificate state `dns_changed`, described as requesting a new certificate; the queried DNS records match GitHub's documented records. Certificate provisioning should finish before any disruptive remove/re-add of the working custom domain is considered. Mobile PageSpeed API requests returned 429, so no speed score or Core Web Vitals pass is claimed.

Ignored local operational aids include a blank lead log, project-evidence template and 264-row historical HTML URL inventory. The inventory is for review, not a guessed redirect map. Original project photos, detailed case studies, confirmed survey coverage and lead-source records still require MKI's input. Business Profile ownership and the exact Houzz profile remain external dependencies.
