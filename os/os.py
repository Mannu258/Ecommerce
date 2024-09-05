import os

directory = os.getcwd()
files = os.listdir(directory)
ext = 0

for filename in files:
    if filename == 'os.py':
        pass
    elif filename.endswith(('.png', '.jpg')):
        new_name = f'image{ext}{os.path.splitext(filename)[1]}'
        os.rename(filename, new_name)
        ext += 1
    else:
        os.remove(filename)

print('All relevant files have been renamed and others removed.')