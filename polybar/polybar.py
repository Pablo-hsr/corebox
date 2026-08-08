from pathlib import Path
import shutil

home = Path.home()

path_polybar = home / '.config' / 'polybar'
path_polybar.mkdir(parents=True, exist_ok=True)

arquivos = [
    Path('polybar') / 'config.ini',
    Path('polybar') / 'config',
    Path('polybar') / 'launch.sh',
]

for arquivo in arquivos:
    shutil.copy(str(arquivo), str(path_polybar / arquivo.name))
