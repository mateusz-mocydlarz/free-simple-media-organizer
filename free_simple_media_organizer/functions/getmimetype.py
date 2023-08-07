# -*- coding: utf-8 -*-
import magic
import filetype
import mimetypes


def get_mimetype(path_to_file: str) -> str:
    """Funkcja zwraca typ mime dla przekazanego pliku"""

    file_mimetype = mimetypes.guess_type(path_to_file)[0]

    if file_mimetype is None:
        file_mimetype = filetype.guess_mime(path_to_file)

        if file_mimetype is None:
            file_mimetype = magic.from_buffer(open(path_to_file, "rb").read(2048), mime=True)

            if file_mimetype is None:
                file_mimetype = "unknow"

    return file_mimetype


if __name__ == "__main__":
    test_file = r"\\Mocny-nas\HDD_MEDIA\2023\2023-06-29 Zagłębocze\ip14\IMG_3608.MOV"
    print(get_mimetype(test_file))
