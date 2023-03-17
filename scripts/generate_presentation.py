from generate_index import index_update
from pathlib import Path
import shutil
import sys
from utils import get_formated_today

def presentation_update(name):
	today = get_formated_today()
	new_folder = Path(f'presentations/{today}_{name}')
	new_folder.mkdir(parents=True, exist_ok=True)
	shutil.copy2('templates/links.html', new_folder)
	shutil.copy2('templates/presentation.html', f'{new_folder}/index.html')
	shutil.copy2('templates/presentation.md', f'{new_folder}/index.md')
	print(f'Presenation {new_folder} created.')

if __name__ == '__main__':
	presentation_update(sys.argv[1])
	index_update()