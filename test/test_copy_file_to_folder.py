import datetime

import pytest


class TestCopyFile:

    @pytest.mark.parametrize("file, folder", [
        ("файл для копирования.txt",
         "FOLDER" + str(datetime.datetime.now()))
    ])
    def test_copy_file_to_folder(self, user_disk_page, file, folder):
        """
        Предусловия : фикстура user_disk_page, выполнена авторизация, открыта страница клиента Яндекс.Диск.
        Шаги:
        1. Создать новую папку и назвать её.
        2. Скопировать файл новую папку.
        ОР : Копия файла (с тем же именем) находится в новой папке.
        """
        user_disk_page\
            .create_folder(folder)\
            .copy_file_to_folder(file, folder)
        assert user_disk_page\
            .file_in_folder(file, folder)
