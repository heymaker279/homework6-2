import requests


def get_oAuth():
    with open("D:/Python/PyCharm/homework6-2/info.txt", "r", encoding="utf-8") as f:
        file = f.read().split("\n")
    yandex_token = file[2]
    ya_url = file[3]
    folder_name = str(file[4])
    return yandex_token, ya_url, folder_name

"""Создание новой папки на яндекс диске"""
def create_new_folder(token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }
    params = {
        "path": f"/{get_oAuth()[2]}"
    }
    response = requests.put(get_oAuth()[1], headers=headers, params=params)
    return response


