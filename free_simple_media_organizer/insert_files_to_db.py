# -*- coding: utf-8 -*-
import os
from time import time
from functions.getmimetype import get_mimetype
from model.db_models import table_mimetypes, table_directories_paths, engine
from sqlalchemy import insert, select

start = time()

# path_to_walk = r"\\Mocny-nas\HDD_MEDIA\2023\2023-06-29 Zagłębocze"
# path_to_walk = r"\\Mocny-nas\HDD_MEDIA" 2395
path_to_walk = r"E:"

files_paths = dict()
mimetypes_list = list()
files_list = list()


for root, dirs, files in os.walk(path_to_walk):
    if len(files) > 0:
        files_paths[root] = files

for path_to_file in files_paths.keys():
    for filename in files_paths[path_to_file]:
        full_path_to_file = os.path.join(path_to_file, filename)
        file_size = os.stat(full_path_to_file).st_size
        mimetype = get_mimetype(full_path_to_file)

        if mimetype not in mimetypes_list:
            mimetypes_list.append(mimetype)


with engine.connect() as conn:
    exists_directories_paths = list()
    exists_mimetypes = list()

    for row in conn.execute(select(table_directories_paths.c["path"])):
        exists_directories_paths.append(row[0])

    for row in conn.execute(select(table_mimetypes.c["mimetype"])):
        exists_mimetypes.append(row[0])

    insert_table_directories_paths = list()
    for path_to_file in files_paths.keys():
        if path_to_file not in exists_directories_paths and len(files_paths[path_to_file]) > 0:
            insert_table_directories_paths.append({"path": path_to_file})

    insert_table_mimetypes = list()
    for mimetype in mimetypes_list:
        if mimetype not in exists_mimetypes:
            insert_table_mimetypes.append({"mimetype": mimetype})

    if len(insert_table_directories_paths) > 0:
        result = conn.execute(insert(table_directories_paths), insert_table_directories_paths)

    if len(insert_table_mimetypes) > 0:
        result = conn.execute(insert(table_mimetypes), insert_table_mimetypes)

    conn.commit()

end = time()
duration = end - start
print(duration)
# print(files_paths)

# if __name__ == "__main__":
#     # test_path = r"/Volumes/HDD_MEDIA/2023"
#     # test_path = r"/Volumes/HDD_MEDIA/2023/2023-06-29 Zagłębocze"
#     test_path = r"\\Mocny-nas\HDD_MEDIA\2023\2023-06-29 Zagłębocze"
