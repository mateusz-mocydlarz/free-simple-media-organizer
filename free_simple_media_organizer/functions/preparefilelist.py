from os import walk

# test_path = r"/Volumes/HDD_MEDIA/2023"
test_path = r"/Volumes/HDD_MEDIA/2023/2023-06-29 Zagłębocze"

files_paths = dict()

for root, dirs, files in walk(test_path):
    if len(files) > 0:
        files_paths[root] = files

print(files_paths)