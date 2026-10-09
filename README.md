# Covalschi Alexei — Design × Code

Responsive, multilingual portfolio site (English, Romanian, Russian). It uses plain HTML, CSS and JavaScript, so it can run without a build step or package installation.

## Preview locally

Open `index.html` in a browser. For a local web server, run `python -m http.server 8000` from this folder, then visit `http://localhost:8000`.

## Add your portfolio files

Copy project images into the matching folders under `public/projects/`:

- `public/projects/maguro/` — Maguro logo, packaging, business cards, mockups and presentation images.
- `public/projects/alart/` — Alart logo, typography, monochrome identity and applications.
- `public/projects/mini/` — mini-projects. Expected names: `simplay.webp`, `aero.webp`, `samurai.webp`, `cyberpunk.webp`, `logos.webp`, `poster.webp`. JPEG equivalents work too.
- `public/projects/anvilcore/` — AnvilCore screenshots.
- `public/certificates/` — certificate images/PDFs.
- `public/documents/` — put the CV here as `Covalschi_Alexei_CV.pdf`.

The experiments gallery currently shows designed typographic placeholders until matching project images are added. The Maguro and Alart covers are CSS compositions, ready to be replaced with original project artwork. Certificate links are enabled once a certificate asset is added. No GitHub address or CV content has been invented.

## Publish

Upload this entire project folder (including `index.html`, `styles.css`, `app.js`, `favicon.svg` and the `public/` folder) to a static host such as Netlify or Cloudflare Pages. Keep `public/` inside the site root because image and document links point into `public/...`. GitHub Pages under a repository subpath needs relative paths or a custom domain.

Google Fonts are loaded remotely; system sans-serif fallbacks are included.
