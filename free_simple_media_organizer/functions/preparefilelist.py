from os import walk, stat, path


def prapere_file_list(path_to_walk):
    """Funkcja zwraca listę plików"""
    files_paths = dict()

    for root, dirs, files in walk(test_path):
        if len(files) > 0:
            files_paths[root] = files

    for path_to_file in files_paths.keys():
        # print(path)
        # print(files_paths[path])
        for filename in files_paths[path_to_file]:
            stat_file = stat(path.join(path_to_file, filename))
            print(stat_file.st_size)


if __name__ == "__main__":
    # test_path = r"/Volumes/HDD_MEDIA/2023"
    # test_path = r"/Volumes/HDD_MEDIA/2023/2023-06-29 Zagłębocze"
    test_path = r"\\Mocny-nas\HDD_MEDIA\2023\2023-06-29 Zagłębocze"
