# -*- coding: utf-8 -*-
import pathlib
import time
from connect_sqlite import connect_sqlite


def insert_media(db_file_path: pathlib.Path, source: pathlib.Path):
    con = connect_sqlite(db_file_path)
    cur = con.cursor()
    cur.execute('''INSERT INTO sources (source_path)
                VALUES (?)''', (source.as_posix(),))
    cur.execute('''SELECT id FROM sources WHERE source_path = ?''', (source.as_posix(),))
    source_id = cur.fetchone()[0]

    insert_data_paths = list()
    prepare_files = dict()
    for root, dirs, files in source.walk():
        if files:
            path = root.as_posix().replace(source.as_posix(), '')
            if len(path) > 0:
                if path[1] == '/':
                    path = path[1:]
            insert_data_paths.append((source_id, path))
            prepare_files[path] = files

    cur.executemany('''INSERT INTO paths (source_id, path)
                    VALUES (?, ?)''', insert_data_paths)

    insert_data_files = list()
    for path_id, path in cur.execute('''SELECT id, path FROM paths WHERE source_id = ?''', (source_id,)):

        for file in prepare_files[path]:
            path = pathlib.Path(path)
            file_path = source.joinpath(path).joinpath(file)
            name = file_path.stem
            extension = file_path.suffix[1:]
            size = file_path.stat().st_size
            insert_data_files.append((path_id, name, extension, size,))

    cur.executemany('''INSERT INTO files (path_id, name, extension, size)
                    VALUES (?, ?, ?, ?)''', insert_data_files)

    con.commit()
    con.close()


if __name__ == "__main__":
    start = time.time()
    db_file_path = pathlib.Path('C:/Users/mateu/Qsync/Programming/tmp_free-simple-media-organizer/db_2/db.db')
    source = pathlib.Path('E:/')
    insert_media(db_file_path, source)
    end = time.time()
    print(end - start)
