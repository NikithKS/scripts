import os

# search for a string inside all files inside directory
# searchStringInDir.py

PATH = ''
ext = ''
requiredString = ''


def scanDir(dir, ext):
    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if(ext == '' or f.path.split('.')[-1] == ext):
                files.append(f.path)

    for dir in list(subfolders):
        sf, f = scanDir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)

    return subfolders, files


sf, files = scanDir(PATH, ext)
count = 0
for path in files:
    with open(path, 'r') as file:
        data = file.read().replace('\n', '')

    if requiredString in data:
        print(path.split('/')[-1])
        count += 1

print("Total: " + str(count))
