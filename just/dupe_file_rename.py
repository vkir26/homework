import shutil
import pathlib


path = pathlib.Path('/just/modules/s')
filename = 'wolf'


file_find = [i for i in [_.name for _ in path.iterdir()] if filename in [i, i.split('.')[0]]]

if len(file_find) != 0:
    for _ in range(1, 11):
        shutil.copy2(f'{path}/{file_find[0]}', f'{path}/{str(_)}.{file_find[0].split(".")[1]}')
    print('Complete!')
else:
    print('File Not Found!')