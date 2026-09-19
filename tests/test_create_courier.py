import requests
import allure
import pytest

from data import Urls, Messages
from generators import generate_random_string


@allure.feature('Создание курьера')
class TestCreateCourier:

    @allure.title('Успешное создание курьера с именем')
    def test_create_courier_with_first_name(self, cleanup_courier):
        with allure.step('Сгенерировать данные для курьера'):
            payload = {
                "login": generate_random_string(),
                "password": generate_random_string(),
                "firstName": generate_random_string(),
            }

        with allure.step('Отправить POST-запрос на создание курьера'):
            response = requests.post(Urls.CREATE_COURIER_URL, data=payload)

        assert response.status_code == 201, (
            f'Получен статус-код {response.status_code}, '
            f'ожидался 201')
        assert response.json() == Messages.CREATE_COURIER_SUCCESS, (
            f'Получен ответ {response.json()}, '
            f'ожидался {Messages.CREATE_COURIER_SUCCESS}')

        # Передаём данные фикстуре, чтобы она удалила курьера после теста
        cleanup_courier.update(payload)


    @allure.title('Успешное создание курьера без имени')
    def test_create_courier_without_first_name(self, cleanup_courier):
        with allure.step('Сгенерировать данные для курьера'):
            payload = {
                "login": generate_random_string(),
                "password": generate_random_string()
            }

        with allure.step('Отправить POST-запрос на создание курьера'):
            response = requests.post(Urls.CREATE_COURIER_URL, data=payload)
      
        assert response.status_code == 201, (
            f'Получен статус-код {response.status_code}, '
            f'ожидался 201')
        assert response.json() == Messages.CREATE_COURIER_SUCCESS, (
            f'Получен ответ {response.json()}, '
            f'ожидался {Messages.CREATE_COURIER_SUCCESS}')
        
        # Передаём данные фикстуре, чтобы она удалила курьера после теста
        cleanup_courier.update(payload)


    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier(self, cleanup_courier):
        with allure.step('Сгенерировать данные для курьера'):
                    payload = {
                        "login": generate_random_string(),
                        "password": generate_random_string(),
                        "firstName": generate_random_string(),
                    }
        
        with allure.step('Отправить первый POST-запрос на создание курьера'):
            response = requests.post(Urls.CREATE_COURIER_URL, data=payload)

        with allure.step('Отправить второй POST-запрос на создание курьера с такими же данными'):
            response = requests.post(Urls.CREATE_COURIER_URL, data=payload)

        assert response.status_code == 409, (
            f'Получен статус-код {response.status_code}, '
            f'ожидался 409')
        assert response.json()['message'] == Messages.CREATE_COURIER_ALREADY_EXISTS, (
            f'Получено сообщение "{response.json()['message']}", '
            f'ожидалось "{Messages.CREATE_COURIER_ALREADY_EXISTS}"')
        
        # Передаём данные фикстуре, чтобы она удалила курьера после теста
        cleanup_courier.update(payload)


    @allure.title('Нельзя создать курьера без обязательного поля login или password')
    @pytest.mark.parametrize('field_to_empty', ['login', 'password'], 
        ids=['without_login', 'without_password'])
    def test_create_courier_missing_fields(self, field_to_empty):
        with allure.step('Сгенерировать данные курьера'):
            payload = {
                "login": generate_random_string(),
                "password": generate_random_string(),
                "firstName": generate_random_string(),
            }

        with allure.step(f'Оставить поле "{field_to_empty}" пустым'):
            payload[field_to_empty] = ""

        with allure.step('Отправить POST-запрос на создание курьера'):
            response = requests.post(Urls.CREATE_COURIER_URL, data=payload)

        assert response.status_code == 400, (
            f'Получен статус-код {response.status_code}, ожидался 400 Bad Request')
        
        assert response.json()['message'] == Messages.CREATE_COURIER_MISSING_FIELDS, (
            f'Получено сообщение "{response.json()['message']}", '
            f'ожидалось "{Messages.CREATE_COURIER_MISSING_FIELDS}"')
        