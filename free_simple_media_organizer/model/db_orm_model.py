# -*- coding: utf-8 -*-
from typing import List
# from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, WriteOnlyMapped


class Base(DeclarativeBase):
    pass


class MimeType(Base):
    __tablename__ = "mime_types"
    id: Mapped[int] = mapped_column(primary_key=True)
    mime: Mapped[str] = mapped_column(String(30))

    # files: Mapped[List["File"]] = relationship(
    #     back_populates="mime_type", cascade="all, delete-orphan"
    # )

    def __repr__(self) -> str:
        return f"MimeType(id={self.id!r}, mime={self.path!r})"


class DirectoriesPaths(Base):
    __tablename__ = "directories_paths"
    id: Mapped[int] = mapped_column(primary_key=True)
    path: Mapped[str] = mapped_column(String(300))

    # files: Mapped[List["File"]] = relationship(
    #     back_populates="path", cascade="all, delete-orphan"
    # )

    def __repr__(self) -> str:
        return f"DirectoriesPaths(id={self.id!r}, path={self.path!r})"


class File(Base):
    __tablename__ = "files"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(300))
    size: Mapped[int] = mapped_column(Integer)

    mime_type_id: Mapped[int] = mapped_column(ForeignKey("mime_types.id"))
    mime_type: WriteOnlyMapped["MimeType"] = relationship(
        cascade="all, delete-orphan",
        passive_deletes=True
    )
    path_id: Mapped[int] = mapped_column(ForeignKey("directories_paths.id"))
    path: WriteOnlyMapped["DirectoriesPaths"] = relationship(
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    def __repr__(self) -> str:
        return f"DirectoriesPaths(id={self.id!r}, name={self.name!r}, size={self.size!r})"

# class User(Base):
#     __tablename__ = "user_account"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30))
#     fullname: Mapped[Optional[str]]
#     addresses: Mapped[List["Address"]] = relationship(
#         back_populates="user", cascade="all, delete-orphan"
#     )
#     def __repr__(self) -> str:
#         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

# class Address(Base):
#     __tablename__ = "address"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email_address: Mapped[str]
#     user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
#     user: Mapped["User"] = relationship(back_populates="addresses")
#     def __repr__(self) -> str:
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"


if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    db_file = r"/Volumes/HDD_DATA/010_Mateusz/programming/tmp_data/free-simple-media-organizer/testowa.db"

    engine = create_engine(f"sqlite:///{db_file}", echo=True)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        file_1 = File(
            name="spongebob.jpg",
            size=500,
            mime_type=MimeType(mime="video"),
            path=DirectoriesPaths(path="testowy")
        )
        file_2 = File(
            name="test.jpg",
            size=5050,
            mime_type=MimeType(mime="image"),
            path=DirectoriesPaths(path="testowy")
        )
        file_3 = File(
            name="twój.jpg",
            size=1500,
            mime_type=MimeType(mime="video"),
            path=DirectoriesPaths(path="testowy_2")
        )
        session.add_all([file_1, file_2, file_3])
        session.commit()
