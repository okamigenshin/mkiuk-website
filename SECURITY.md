# Website security

This is a public static website. It has no login, backend, database or online payment processing. Public repository visibility lets people read source files; it does not grant write access.

## Controls

- Changes to `main` go through a pull request and the required Site safety check. Branch deletion and force pushes are blocked, including for the owner. No routine bypass is configured.
- Site safety checks the six pages, local resources, browser restrictions and publishing domain. It also scans Git history with Gitleaks; reports redact secret values. Private keys, environment files, databases and recovery material must stay outside Git.
- Workflow tokens default to read-only and cannot approve pull requests. Outside contributors need maintainer approval before workflows run. External Actions are restricted to GitHub-owned Actions and must use full commit SHAs. Dependabot checks Action versions monthly.
- Pull requests cannot publish. Publishing runs only from `main`, depends on successful safety checks, and uses the `github-pages` environment restricted to `main`. Only public HTML, CSS, JavaScript and assets enter the deployment artifact.
- Every page has a Content Security Policy that allows local scripts and the existing Google Fonts resources. Inline script execution, eval, plugins, base URL changes and form submissions are not permitted. Referrer information is withheld.
- HTTPS is enforced. The custom domain must remain verified in the owner's GitHub Pages account; retain its DNS verification TXT record.

## Operations

The only human repository administrator is `okamigenshin`. GitHub account 2FA and passkeys were confirmed enabled on 8 October 2026. Keep recovery codes in a secure personal location. Add collaborators only when needed and give the minimum access required. These controls cannot prevent misuse of a compromised owner account, which can edit repository settings.

Never commit credentials, private client files or production exports. If a secret is exposed, revoke or rotate it before dealing with repository history. Use a trusted private channel to report a suspected exposure; do not paste secrets into public issues.

## Hosting limits

GitHub Pages does not offer project-configurable HTTP response headers. The HTML CSP provides browser restrictions, but `frame-ancestors` and headers such as a custom Permissions Policy need a host or proxy that supports response-header configuration. This site does not claim those controls are present. The public website's HTML, CSS, JavaScript and images remain downloadable even if repository visibility changes.

Checks reduce risk, but no repository is guaranteed completely secure. Re-run checks on changes, apply security updates, and periodically review access and domain ownership.
