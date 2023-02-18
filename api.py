import requests
import json

class Reqres:
    def __init__(self):
        self.base_url = 'https://reqres.in/'

    def post_register_user(self, email: str, password: str) -> json:
        """Метод делает запрос к API сервера, возвращает статус запроса и результат в формате
                        JSON с уникальным id пользователя"""
        data = {'email': email, 'password': password}
        res = requests.post(self.base_url + 'api/register', data=data)
        status = res.status_code
        result = ''

        try:
            result = res.json()
        except:
            result = res.text

        return status, result

        return status, result

    def post_create_user(self, name: str, job: str) -> json:
        """Метод делает запрос к API сервера, возвращает статус запроса и результат в формате
                JSON с уникальным id, name, job, createdAt пользователя"""

        data = {'name': name, 'job': job}
        res = requests.post(self.base_url + 'api/users', data=data)
        status = res.status_code
        result = ''

        try:
            result = res.json()
        except:
            result = res.text

        return status, result

    def put_user(self, name, job):
        """Метод делает запрос к API сервера, возвращает статус запроса и результат в формате
                        JSON с измененными данными name или job"""

        data = {'name': name, 'job': job}
        res = requests.put(self.base_url + 'api/users/2', data=data)
        status = res.status_code
        result = ''

        try:
            result = res.json()
        except:
            result = res.text

        return status, result