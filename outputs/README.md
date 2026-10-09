# Covalschi Alexei â€” Design Ã— Code

Responsive, multilingual portfolio site (English, Romanian, Russian). It uses plain HTML, CSS and JavaScript, so it can run without a build step or package installation.

## Preview locally

Open `index.html` in a browser. For a local web server, run `python -m http.server 8000` from this folder, then visit `http://localhost:8000`.

## Add your portfolio files

Portfolio materials added:

- `public/projects/alart/alart-preview.png` and `alart-presentation.pdf` — Alart preview and presentation (2025).
- `public/projects/maguro/maguro-preview.png` and `maguro-presentation.pdf` — Maguro preview and presentation (2026).
- `public/projects/other/work-01.png` through `work-04.png` — Simplay, Aero, Samurai, and Cyberpunk. The gallery also uses optimized WebP copies for the two large posters.
- `public/projects/zakalka/zakalka-dashboard.webp` — Zakalka project preview; its card links to the published site.
- `public/documents/Covalschi_Alexei_CV.pdf` — CV download.
- `public/certificates/` — add certificate images/PDFs here when available.

To replace a project, keep its current filename or update the matching path in `index.html` or `app.js`.

## Publish

Upload this entire project folder (including `index.html`, `styles.css`, `app.js`, `favicon.svg` and the `public/` folder) to a static host such as Netlify or Cloudflare Pages. Keep `public/` inside the site root because image and document links point into `public/...`. GitHub Pages under a repository subpath needs relative paths or a custom domain.

Google Fonts are loaded remotely; system sans-serif fallbacks are included.
