import unittest
import requests
from application.Yandex_Disk import get_oAuth

"""Получаем код ответа на запрос о наличии на диске новой созданной папки"""
def check_new_folder() -> int:
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(get_oAuth()[0])
    }
    params = {
        "path": f"/{get_oAuth()[2]}"
    }
    response = requests.get(get_oAuth()[1], headers=headers, params=params).status_code
    if response != 200:
        raise TypeError
    return response


class TestResponseCode(unittest.TestCase):
    '''Тест проверки кода ответа '''

    def test_check_new_folder_success(self): # проверка на успешное выполнение функции
        self.assertEqual(check_new_folder(), 200)

    def test_check_new_folder_fail(self): # проверка на неправильный ответ
        self.assertNotEqual(check_new_folder(), '200')
        self.assertNotEqual(check_new_folder(), 409)


