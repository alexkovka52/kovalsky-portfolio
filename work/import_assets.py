from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs" / "public" / "projects"

def webp(source: Path, target: Path, max_edge: int = 1800):
    with Image.open(source) as im:
        im = im.convert("RGB")
        im.thumbnail((max_edge, max_edge), Image.Resampling.LANCZOS)
        target.parent.mkdir(parents=True, exist_ok=True)
        im.save(target, "WEBP", quality=86, method=6)
        print(f"{target.relative_to(ROOT)}: {im.width}x{im.height}, {target.stat().st_size:,} bytes")

for slug in ("simplay", "aero", "samurai", "cyberpunk"):
    webp(ROOT / "work" / f"{slug}.png", OUTPUT / "mini" / f"{slug}.webp")

webp(ROOT / "work" / "pdf-review" / "maguro" / "page-01.jpg", OUTPUT / "maguro" / "cover.webp", 1800)
webp(ROOT / "work" / "pdf-review" / "alart" / "page-01.jpg", OUTPUT / "alart" / "cover.webp", 1800)
