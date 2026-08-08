from pathlib import Path
import shutil


with open('.xinitrc', 'w') as f:
    f.write('exec i3\n')

source_file = Path('.xinitrc')
home = Path.home()
destination_file = home / source_file.name

shutil.move(str(source_file), str(destination_file))

#configuração do I3

path_i3 = home / '.config' / 'i3'
path_i3.mkdir(parents=True, exist_ok=True)

arquivos = [
    Path('display') / 'config',
]

for arquivo in arquivos:
    shutil.copy(str(arquivo), str(path_i3 / arquivo.name))