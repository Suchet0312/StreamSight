import json
from pathlib import Path

nb_path = Path(__file__).resolve().parents[1] / 'notebooks' / '03_eda.ipynb'
nb = json.loads(nb_path.read_text(encoding='utf-8'))
updated_id = 0
updated_lang = 0
for cell in nb.get('cells', []):
    # ensure metadata exists
    md = cell.setdefault('metadata', {})
    # ensure metadata.id exists (use top-level id if present)
    if 'id' not in md:
        top_id = cell.get('id') or md.get('id')
        if top_id:
            md['id'] = top_id
            updated_id += 1
    # ensure metadata.language exists
    if 'language' not in md:
        if cell.get('cell_type') == 'code':
            md['language'] = 'python'
        else:
            md['language'] = 'markdown'
        updated_lang += 1

# write back
nb_path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(f'updated_id={updated_id}, updated_lang={updated_lang}, total_cells={len(nb.get("cells",[]))}')
