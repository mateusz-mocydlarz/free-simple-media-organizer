# -*- coding: utf-8 -*-
import os
from time import time
from functions.getmimetype import get_mimetype
from model.db_core_model import table_mimes, table_paths, table_files
from sqlalchemy import insert, select, create_engine

start = time()

# path_to_walk = r"\\Mocny-nas\HDD_MEDIA\2023\2023-06-29 Zagłębocze"
# path_to_walk = r"\\Mocny-nas\HDD_MEDIA" 2395
# path_to_walk = r"E:"
path_to_walk = r"/Volumes/HDD_MEDIA/2023/2023-06-29 Zagłębocze"
# path_to_walk = r"/Volumes/HDD_MEDIA/2023"
db_file = r"/Volumes/HDD_DATA/010_Mateusz/programming/tmp_data/free-simple-media-organizer/mac_testowa.db"

engine = create_engine(f"sqlite:///{db_file}", echo=True)

# pobranie istniejących ścieżek i mime z bazy
with engine.connect() as conn:
    exists_paths = list()
    id_path = dict()
    for row in conn.execute(select(table_paths.c["id"], table_paths.c["path"])):
        exists_paths.append(row[1])
        id_path[row[1]] = row[0]

    exists_mime = list()
    id_mime = dict()
    for row in conn.execute(select(table_mimes.c["id"], table_mimes.c["mime"])):
        exists_mime.append(row[1])
        id_mime[row[1]] = row[0]
    
    for row in conn.execute(select(
                table_files.c["id"],
                table_files.c["name"],
                table_files.c["size"],
                table_files.c["path_id"],
                table_files.c["mime_id"]
                # table_paths.c["path"]
            ).join(table_paths).where(table_paths.c["path"].like(f"{ path_to_walk }%"))):
        pass

list_all_files = list()
list_mime_to_insert = list()
list_paths_to_insert = list()

# zebranie wszystkich plików i ścieżek
for root, dirs, files in os.walk(path_to_walk):
    for file in files:
        path_to_file = os.path.join(root, file)
        mime = get_mimetype(path_to_file)
        file_info = {
            "name": file,
            "size": os.stat(path_to_file).st_size,
            "mime": mime,
            "path": root
        }
        if mime.split("/")[0] in ["image", "video"]:
            list_all_files.append(file_info)

            # jeśli ścieżka nie istnieje w bazie, to przygotować do insertu
            if root not in exists_paths and {"path": root} not in list_paths_to_insert:
                list_paths_to_insert.append({"path": root})

            # jeśli mime nie istnieje w bazie, to przygotować do insertu
            if mime not in exists_mime and {"mime": mime} not in list_mime_to_insert:
                list_mime_to_insert.append({"mime": mime})


# insert tylko jeśli trzeba i dopisanie nowych do bazy
if len(list_paths_to_insert) > 0 or len(list_mime_to_insert) > 0:
    with engine.connect() as conn:
        if len(list_paths_to_insert) > 0:
            result = conn.execute(insert(table_paths).returning(
                table_paths.c["id"], table_paths.c["path"]), list_paths_to_insert
            )
            for row in result:
                id_path[row[1]] = row[0]
            conn.commit()

        if len(list_mime_to_insert) > 0:
            result = conn.execute(insert(table_mimes).returning(
                table_mimes.c["id"], table_mimes.c["mime"]), list_mime_to_insert
            )
            for row in result:
                id_mime[row[1]] = row[0]
            conn.commit()

# przygotowanie danych o plikach do insertu
for i, f in enumerate(list_all_files):
    list_all_files[i]["path_id"] = id_path[f["path"]]
    list_all_files[i]["mime_id"] = id_mime[f["mime"]]
    del list_all_files[i]["path"]
    del list_all_files[i]["mime"]

with engine.connect() as conn:
    if len(list_all_files) > 0:
        result = conn.execute(insert(table_files), list_all_files)
        conn.commit()

print(time() - start)
