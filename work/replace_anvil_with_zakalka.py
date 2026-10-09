from pathlib import Path
import re

root = Path(__file__).resolve().parents[1] / "outputs"
url = "https://zaakalk.vercel.app/"
html_path = root / "index.html"
html = html_path.read_text(encoding="utf-8")
section = f'''<section class="anvil section" id="zakalka"><div class="section-head mono"><span>05 / <span data-i="sections.frontend">WEBSITE PROJECT</span></span><span data-i="zakalka.meta">LIVE WEBSITE / 2026</span></div><div class="anvil-layout"><div class="anvil-copy"><p class="mono project-type" data-i="zakalka.category">WEB PROJECT / FITNESS TRACKER</p><h2>ZAKAL<span>KA</span></h2><p data-i="zakalka.desc">A fitness tracking website for workouts, nutrition, daily goals and progress.</p><div class="tech-list mono" data-i="zakalka.features">WORKOUTS · NUTRITION · GOALS · PROGRESS</div><a class="text-link" href="{url}" target="_blank" rel="noopener noreferrer"><span data-i="zakalka.link">VISIT WEBSITE</span> <b>↗</b></a></div><div class="anvil-preview zakalka-preview"><a href="{url}" target="_blank" rel="noopener noreferrer"><img src="public/projects/zakalka/zakalka-dashboard.webp" alt="Zakalka fitness dashboard with workout, nutrition, and progress panels" loading="lazy"></a></div></div></section>'''
html, count = re.subn(r'<section class="anvil section">.*?</section>', section, html, count=1, flags=re.S)
if count != 1:
    raise RuntimeError(f"Expected to replace one AnvilCore section, found {count}")
html_path.write_text(html, encoding="utf-8")

app_path = root / "app.js"
app = app_path.read_text(encoding="utf-8")
replacements = {
    "'sections.frontend':'FRONTEND PROJECT'": "'sections.frontend':'WEBSITE PROJECT','zakalka.meta':'LIVE WEBSITE / 2026','zakalka.category':'WEB PROJECT / FITNESS TRACKER','zakalka.desc':'A fitness tracking website for workouts, nutrition, daily goals and progress.','zakalka.features':'WORKOUTS · NUTRITION · GOALS · PROGRESS','zakalka.link':'VISIT WEBSITE'",
    "'sections.frontend':'PROIECT FRONTEND'": "'sections.frontend':'PROIECT WEB','zakalka.meta':'SITE WEB LIVE / 2026','zakalka.category':'PROIECT WEB / FITNESS','zakalka.desc':'Un site pentru urmărirea antrenamentelor, alimentației, obiectivelor și progresului.','zakalka.features':'ANTRENAMENTE · NUTRIȚIE · OBIECTIVE · PROGRES','zakalka.link':'VIZITEAZĂ SITE-UL'",
    "'sections.frontend':'FRONTEND-ПРОЕКТ'": "'sections.frontend':'ВЕБ-ПРОЕКТ','zakalka.meta':'ЖИВОЙ САЙТ / 2026','zakalka.category':'ВЕБ-ПРОЕКТ / ФИТНЕС','zakalka.desc':'Сайт для отслеживания тренировок, питания, ежедневных целей и прогресса.','zakalka.features':'ТРЕНИРОВКИ · ПИТАНИЕ · ЦЕЛИ · ПРОГРЕСС','zakalka.link':'ОТКРЫТЬ САЙТ'",
}
for old, new in replacements.items():
    if old not in app:
        raise RuntimeError(f"Translation anchor not found: {old}")
    app = app.replace(old, new, 1)
app_path.write_text(app, encoding="utf-8")

css_path = root / "styles.css"
css = css_path.read_text(encoding="utf-8")
css += "\n.zakalka-preview{padding:0;min-height:0;overflow:hidden;transform:none}.zakalka-preview>a{display:block;line-height:0}.zakalka-preview img{display:block;width:100%;height:auto;transition:transform .45s}.zakalka-preview:hover img{transform:scale(1.015)}\n"
css_path.write_text(css, encoding="utf-8")
