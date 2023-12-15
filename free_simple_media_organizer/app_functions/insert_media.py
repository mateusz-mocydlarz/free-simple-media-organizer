# -*- coding: utf-8 -*-
import pathlib
import sqlite3
import time


def insert_media(con, source: pathlib.Path, app_user: str):
    # con = sqlite3.connect('C:/Users/mateu/Qsync/Programming/tmp_free-simple-media-organizer/db/db.db')
    cur = con.cursor()
    cur.execute('''INSERT INTO sources (source_path, created_by, modified_by)
                VALUES (?, ?, ?)''', (source.as_posix(), app_user, app_user,))
    cur.execute('''SELECT id FROM sources WHERE source_path = ?''', (source.as_posix(),))
    source_id = cur.fetchone()[0]
    # print(source_id)

    i = 0
    insert_data_paths = list()
    prepare_files = dict()
    for root, dirs, files in source.walk():
        if files:
            path = root.as_posix().replace(source.as_posix(), '')
            if len(path) > 0:
                if path[1] == '/':
                    path = path[1:]
            insert_data_paths.append((source_id, path, app_user, app_user,))
            prepare_files[path] = files

        # print("----")
        # print(root.as_posix())
        # # print(path)
        # print(dirs)
        # print(files)
        # i += 1
        # if i > 3:
        #     break
    # print(prepare_files)
    cur.executemany('''INSERT INTO paths (source_id, path, created_by, modified_by)
                    VALUES (?, ?, ?, ?)''', insert_data_paths)

    insert_data_files = list()
    for path_id, path in cur.execute('''SELECT id, path FROM paths WHERE source_id = ?''', (source_id,)):
        # print(f"{path_id} - {path} - {source}")

        for file in prepare_files[path]:
            # print("===========")
            # print(f"source = '{source}'")
            # print(f"path = '{path}'")
            path = pathlib.Path(path)
            # print(path)
            file_path = source.joinpath(path).joinpath(file)
            # print(file_path)
            name = file_path.stem
            extension = file_path.suffix[1:]
            size = file_path.stat().st_size
            insert_data_files.append((path_id, name, extension, size, app_user, app_user,))

    # print(insert_data_files)

    cur.executemany('''INSERT INTO files (path_id, name, extension, size, created_by, modified_by)
                    VALUES (?, ?, ?, ?, ?, ?)''', insert_data_files)

    con.commit()


if __name__ == "__main__":
    start = time.time()
    from connect_sqlite import connect_sqlite
    import getpass
    import socket
    con = connect_sqlite('C:/Users/mateu/Qsync/Programming/tmp_free-simple-media-organizer/db/db.db')
    source = pathlib.Path('E:/')
    APP_USER = f'{socket.gethostname()}/{getpass.getuser()}'
    insert_media(con, source, APP_USER)
    con.close()
    end = time.time()
    print(end - start)
