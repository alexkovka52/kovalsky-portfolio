from pathlib import Path
import re

path = Path(__file__).resolve().parents[1] / "outputs" / "index.html"
html = path.read_text(encoding="utf-8")
for slug, filename in (("maguro", "maguro-case-study.pdf"), ("alart", "alart-case-study.pdf")):
    start = html.index(f'<article class="project-card {slug}"')
    end = html.index("</article>", start) + len("</article>")
    card = re.sub(r'<a class="case-link text-link"[^>]*>.*?</a>', "", html[start:end])
    team_end = card.index("</p>", card.index('<p class="project-team"')) + len("</p>")
    link = f'<a class="case-link text-link" href="public/projects/{slug}/{filename}" target="_blank" rel="noreferrer" data-i="work.case">VIEW CASE STUDY</a>'
    card = card[:team_end] + link + card[team_end:]
    html = html[:start] + card + html[end:]
path.write_text(html, encoding="utf-8")
