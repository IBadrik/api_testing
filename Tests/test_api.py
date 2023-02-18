from api import Reqres

req = Reqres()

def test_post_register_user(email='eve.holt@reqres.in', password='pistol'):
    """Проверяю что запрос api ключа возвращает статус 200 и в результате содержится id и token"""

    # Отправляю запрос и сохраняю полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = req.post_register_user(email, password)
    # Сверяю полученные данные с ожиданиями
    assert status == 200
    assert 'id' and 'token' in result

def test_post_create_user(name='ilias', job='QA'):
    """Проверяю что запрос api ключа возвращает статус 201 и в результате содержится id"""

    status, result = req.post_create_user(name, job)
    # Сверяю полученные данные с ожиданиями
    assert status == 201
    assert 'id' and 'name' and 'job' and 'createdAt' in result

def test_put_user(name='ilias', job='Builder'):
    """Проверяю что запрос api ключа возвращает статус 200 и в результате изменяется job"""

    status, result = req.put_user(name, job)

    assert status == 200
    assert 'updatedAt' in result



