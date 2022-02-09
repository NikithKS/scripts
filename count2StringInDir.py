import os

# Count 2 strings inside all files inside directory and check if they are equal
# count2StringInDir.py

PATH = ''
ext = ''
str1 = ''
str2 = ''


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
for path in files:
    with open(path, 'r') as file:
        data = file.read().replace('\n', '')

    count1 = data.count(str1)
    count2 = data.count(str2)
#     count2 = 2

    if(count1 != count2):
        print(path.split('/')[-1])
        print(count1, count2)
