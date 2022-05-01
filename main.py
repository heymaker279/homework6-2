from application.Yandex_Disk import get_oAuth, create_new_folder


if __name__ == "__main__":
    create_new_folder(get_oAuth()[0])


