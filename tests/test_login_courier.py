import requests
import allure
import pytest

from data import Urls, Messages


@allure.feature('Логин курьера')
class TestLoginCourier:

    @allure.title('Успешный логин курьера')
    def test_login_courier(self, create_and_delete_courier):
        with allure.step('Сформировать данные для авторизации курьера'):
            payload = {
                "login": create_and_delete_courier["login"],
                "password": create_and_delete_courier["password"]
            }
        with allure.step('Отправить POST-запрос на логин курьера'):
            response = requests.post(Urls.LOGIN_COURIER_URL, data=payload)
            
            assert response.status_code == 200, (
                f'Получен статус-код {response.status_code}, '
                f'ожидался 200 OK')
            assert 'id' in response.json(), (
                f'В ответе нет ключа "id". Получен ответ: {response.json()}')

    @allure.title('Нельзя авторизовать курьера без обязательного поля login или password')
    @pytest.mark.parametrize('field_to_empty', ['login', 'password'], 
        ids=['empty_login', 'empty_password'])
    def test_login_courier_missing_fields(self, field_to_empty, create_and_delete_courier):
        with allure.step('Сформировать данные для авторизации курьера'):
            payload = {
                "login": create_and_delete_courier["login"],
                "password": create_and_delete_courier["password"]
            }
        with allure.step(f'Сделать поле "{field_to_empty}" пустым'):
            payload[field_to_empty] = ""
        with allure.step('Отправить POST-запрос на логин курьера'):
            response = requests.post(Urls.LOGIN_COURIER_URL, data=payload, timeout=30)

        assert response.status_code == 400, (
            f'Получен статус-код {response.status_code}, ожидался 400 Bad Request')
                    
        assert response.json()['message'] == Messages.LOGIN_COURIER_MISSING_FIELDS, (
            f'Получено сообщение "{response.json()['message']}", '
            f'ожидалось "{Messages.LOGIN_COURIER_MISSING_FIELDS}"')

    @allure.title('Неверный login или password')
    @pytest.mark.parametrize('invalid_field', ['login', 'password'], 
        ids=['invalid_login', 'invalid_password'])
    def test_login_courier_with_invalid_field(self, invalid_field, create_and_delete_courier):
        with allure.step('Сформировать данные для авторизации курьера'):
            payload = {
                "login": create_and_delete_courier["login"],
                "password": create_and_delete_courier["password"]
            }
        with allure.step(f'Сделать поле "{invalid_field}" несоответсвующем паре логин-пароль'):
            payload[invalid_field] = payload[invalid_field] + "x"
        with allure.step('Отправить POST-запрос на логин курьера'):
            response = requests.post(Urls.LOGIN_COURIER_URL, data=payload, timeout=30)
    
        assert response.status_code == 404, (
            f'Получен статус-код {response.status_code}, ожидался 404 Not Found')
                        
        assert response.json()['message'] == Messages.LOGIN_COURIER_NOT_FOUND, (
            f'Получено сообщение "{response.json()['message']}", '
            f'ожидалось "{Messages.LOGIN_COURIER_NOT_FOUND}"')
        