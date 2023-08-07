from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

tmp_path = r"\\Mocny-nas\hdd_data\010_Mateusz\programming\tmp_data\free-simple-media-organizer\test.db"

engine = create_engine(f"sqlite:///{tmp_path}", echo=True)
metadata_obj = MetaData()

# ścieżki do katalogów z plikami
table_directories_paths = Table(
    "directories_paths",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("path", String(300), nullable=False)
)

# słownik z typami plików
table_files_types = Table(
    "files_types",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("filetype", String(30), nullable=False),
)

# podstawowe informacja o plikach
table_files = Table(
    "files",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("directories_paths_id", ForeignKey("directories_paths.id"), nullable=False),
    Column("files_types_id", ForeignKey("files_types.id"), nullable=False),
    Column("filename", String(300), nullable=False),
    Column("filesize", Integer, nullable=False)
)

metadata_obj.drop_all(engine)
metadata_obj.create_all(engine)

# with engine.connect() as conn:
#     pass
