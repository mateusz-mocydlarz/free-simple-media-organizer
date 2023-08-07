from sqlalchemy import (create_engine, MetaData, Table, Column, Integer, String, ForeignKey, insert,
                        UniqueConstraint, DateTime)
from datetime import datetime
import socket

tmp_path = r"\\Mocny-nas\hdd_data\010_Mateusz\programming\tmp_data\free-simple-media-organizer\test.db"

engine = create_engine(f"sqlite:///{tmp_path}", echo=True)
metadata_obj = MetaData()

# informacje o bazie danych
table_db_informations = Table(
    "db_informations",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("information", String(50), nullable=False, unique=True),
    Column("value", String(50), nullable=False),
    comment="Informacje o bazie danych"
)

# ścieżki do katalogów z plikami
table_directories_paths = Table(
    "directories_paths",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("path", String(300), nullable=False, unique=True),

    # techniczne kolumny
    Column("db_creation_date", DateTime, nullable=False, default=datetime.now()),
    Column("db_creation_hostname", String(50), nullable=False, default=socket.gethostname()),
    Column("db_modification_date", DateTime, nullable=False, default=datetime.now()),
    Column("db_modification_hostname", String(50), nullable=False, default=socket.gethostname()),
    comment="Ścieżki do katalogów z plikami"
)

# słownik z typami plików
table_mimetypes = Table(
    "miemetypes",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("mimetype", String(30), nullable=False),

    # techniczne kolumny
    Column("db_creation_date", DateTime, nullable=False, default=datetime.now()),
    Column("db_creation_hostname", String(50), nullable=False, default=socket.gethostname()),
    Column("db_modification_date", DateTime, nullable=False, default=datetime.now()),
    Column("db_modification_hostname", String(50), nullable=False, default=socket.gethostname()),
    comment="Słownik z typami plików"
)

# podstawowe informacja o plikach
table_files = Table(
    "files",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("directorie_path_id", ForeignKey("directories_paths.id"), nullable=False),
    Column("mimetype_id", ForeignKey("miemetypes.id"), nullable=False),
    Column("filename", String(300), nullable=False),
    Column("filesize", Integer, nullable=False),

    # techniczne kolumny
    Column("db_creation_date", DateTime, nullable=False, default=datetime.now()),
    Column("db_creation_hostname", String(50), nullable=False, default=socket.gethostname()),
    Column("db_modification_date", DateTime, nullable=False, default=datetime.now()),
    Column("db_modification_hostname", String(50), nullable=False, default=socket.gethostname()),
    comment="Podstawowe informacja o plikach"
)

# szczegółowe informacje o plikach
table_files_metadata = Table(
    "files_metadata",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("file_id", ForeignKey("files.id"), nullable=False),
    Column("tag", String(50), nullable=False),
    Column("value", String, nullable=False),
    UniqueConstraint("file_id", "tag", name="uix_fm"),

    # techniczne kolumny
    Column("db_creation_date", DateTime, nullable=False, default=datetime.now()),
    Column("db_creation_hostname", String(50), nullable=False, default=socket.gethostname()),
    Column("db_modification_date", DateTime, nullable=False, default=datetime.now()),
    Column("db_modification_hostname", String(50), nullable=False, default=socket.gethostname()),
    comment="Szczegółowe informacje o plikach"
)

if __name__ == "__main__":
    metadata_obj.drop_all(engine)
    metadata_obj.create_all(engine)

    with engine.connect() as conn:
        result = conn.execute(
            insert(table_db_informations),
            [
                {"information": "create_date_db", "value": "2023-08-07"},
                {"information": "app_version", "value": "v1.00.00"},
            ],
        )
        # result = conn.execute(
        #     insert(table_directories_paths),
        #     [
        #         {"path": "testowy"},
        #         {"path": "testowy_2"},
        #     ],
        # )
        conn.commit()
