"""Regenerate the static gallery manifest without third-party dependencies."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.avif', '.svg', '.bmp'}
excluded = {'.git', 'node_modules', '.venv', 'venv'}
images = sorted(
    path.relative_to(root).as_posix()
    for path in root.rglob('*')
    if not excluded.intersection(path.relative_to(root).parts)
    and path.is_file() and path.suffix.lower() in extensions
)
(root / 'images.json').write_text(json.dumps(images, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Indexed {len(images)} images.')
