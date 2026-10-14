"""Build one HTML page per Markdown source with shared chapter navigation."""
import html
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import quote

base = sys.argv[1].rstrip('/')
sources = [Path(filename) for filename in sys.argv[2:]]
index = sources[0].read_text(encoding='utf-8')
site_title = re.search(r'^title: (.+)$', index, re.M).group(1)
icon = '<svg class="pencil-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m16 3 5 5-12 12-6 1 1-6Z M14 5l5 5"/></svg>'
chapters = []
for source in sources:
    heading = re.search(r'^# (.+)$', source.read_text(encoding='utf-8'), re.M)
    chapters.append((source, heading.group(1) if heading else 'Startseite'))

for source, title in chapters:
    navigation = '<ul>' + ''.join(
        '<li><a href="' + html.escape(item.stem + '.html', quote=True) + '"' +
        (' aria-current="page"' if item == source else '') + '>' +
        html.escape(label) + '</a></li>' for item, label in chapters
    ) + '</ul>'
    metadata = {
        'title': site_title, 'lang': 'de',
        'pagetitle': title + ' · ' + site_title,
        'chapter-navigation': '`' + navigation + '`{=html}',
        'edit-index-url': base + '/pages/index.md',
        'edit-page-url': base + '/' + quote(source.as_posix(), safe='/'),
        'pencil-icon': '`' + icon + '`{=html}',
    }
    with tempfile.TemporaryDirectory() as directory:
        metadata_path = Path(directory) / 'metadata.json'
        metadata_path.write_text(json.dumps(metadata), encoding='utf-8')
        subprocess.run([
            'pandoc', '--from=markdown', '--standalone', '--toc', '--toc-depth=3',
            '--resource-path=.:pages', '--to=html5', '--template=scripts/page.html',
            '--lua-filter=scripts/alerts.lua',
            '--metadata-file=' + str(metadata_path), str(source),
            '--output=_site/' + source.stem + '.html',
        ], check=True)
