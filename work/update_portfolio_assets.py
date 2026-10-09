from pathlib import Path
import re

root = Path(__file__).resolve().parents[1] / "outputs"
html_path = root / "index.html"
app_path = root / "app.js"
css_path = root / "styles.css"

html = html_path.read_text(encoding="utf-8")
html = html.replace(
    '<div class="project-visual visual-maguro">',
    '<div class="project-visual visual-maguro"><img class="project-cover" src="public/projects/maguro/cover.webp" alt="Maguro logo, cover from the project presentation" loading="lazy">',
)
html = html.replace(
    '<div class="project-visual visual-alart">',
    '<div class="project-visual visual-alart"><img class="project-cover" src="public/projects/alart/cover.webp" alt="Alart logo, cover from the project presentation" loading="lazy">',
)
for slug, filename in (("maguro", "maguro-case-study.pdf"), ("alart", "alart-case-study.pdf")):
    start = html.index(f'<article class="project-card {slug}"')
    end = html.index("</article>", start) + len("</article>")
    card = html[start:end]
    card = re.sub(r'<a class="case-link text-link"[^>]*>.*?</a>', "", card)
    team_end = card.index("</p>", card.index('<p class="project-team"')) + len("</p>")
    link = f'<a class="case-link text-link" href="public/projects/{slug}/{filename}" target="_blank" rel="noreferrer" data-i="work.case">VIEW CASE STUDY</a>'
    card = card[:team_end] + link + card[team_end:]
    html = html[:start] + card + html[end:]
html = html.replace('<p class="gallery-note mono" data-i="gallery.note">PROJECT ARTWORK WILL APPEAR HERE WHEN ADDED TO /public/projects/mini/</p>', '')
html_path.write_text(html, encoding="utf-8")

app = app_path.read_text(encoding="utf-8")
app = app.replace("'work.team':'Team project with Cuciuc Artiom'", "'work.team':'Team project with Cuciuc Artiom','work.case':'VIEW CASE STUDY'")
app = app.replace("'work.team':'Proiect de echipă cu Cuciuc Artiom'", "'work.team':'Proiect de echipă cu Cuciuc Artiom','work.case':'VEZI PREZENTAREA'")
app = app.replace("'work.team':'Командный проект с Cuciuc Artiom'", "'work.team':'Командный проект с Cuciuc Artiom','work.case':'СМОТРЕТЬ ПРЕЗЕНТАЦИЮ'")
app = app.replace("['cyberpunk','CYBERPUNK','fan art'],['logos','LOGOS','explorations'],['poster','GRAPHIC','study']", "['cyberpunk','CYBERPUNK','fan art']")
app = app.replace("${String(galleryIndex+1).padStart(2,'0')} / 06 —", "${String(galleryIndex+1).padStart(2,'0')} / ${String(galleryItems.length).padStart(2,'0')} —")
app_path.write_text(app, encoding="utf-8")

css = css_path.read_text(encoding="utf-8")
css += "\n.project-cover{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}.visual-maguro>.project-cover~*,.visual-alart>.project-cover~*{display:none}.project-visual.visual-maguro,.project-visual.visual-alart{background:#181817}.case-link{margin-top:12px;padding:8px 0;font-size:8px}.project-info>div:first-child{max-width:75%}\n"
css_path.write_text(css, encoding="utf-8")
