from sqlalchemy import (MetaData, Table, Column, Integer, String, ForeignKey,
                        UniqueConstraint, DateTime)
from datetime import datetime
import socket

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
table_paths = Table(
    "paths",
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
table_mimes = Table(
    "mimes",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("mime", String(30), nullable=False),

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
    Column("name", String(300), nullable=False),
    Column("size", Integer, nullable=False),
    Column("path_id", ForeignKey("paths.id"), nullable=False),
    Column("mime_id", ForeignKey("mimes.id"), nullable=False),
    UniqueConstraint("name", "path_id", name="uix_f"),

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
    from sqlalchemy import create_engine, insert
    db_file = r"/Volumes/HDD_DATA/010_Mateusz/programming/tmp_data/free-simple-media-organizer/mac_testowa.db"

    engine = create_engine(f"sqlite:///{db_file}", echo=True)
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
