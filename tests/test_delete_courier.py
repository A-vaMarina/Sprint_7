import requests
import allure

from data import Urls, Messages
from helpers import register_new_courier, get_courier_id


@allure.feature('Удаление курьера')
class TestDeleteCourier:

    @allure.title('Успешное удаление курьера')
    def test_delete_courier(self):
        with allure.step('Создать нового курьера'):
            courier = register_new_courier()

        with allure.step('Получить id курьера'):
            courier_id = get_courier_id(courier["login"], courier["password"])

        with allure.step('Отправить DELETE-запрос на удаление курьера'):
            response = requests.delete(f"{Urls.DELETE_COURIER_URL}{courier_id}")

        assert response.status_code == 200, (
            f'Получен статус-код {response.status_code}, '
            f'ожидался 200 OK')
        assert response.json() == Messages.DELETE_COURIER_SUCCESS, (
            f'Получен ответ {response.json()}, '
            f'ожидался {Messages.DELETE_COURIER_SUCCESS}')


    @allure.title('Ошибка, если не передан id курьера')
    def test_delete_courier_without_courier_id(self):
        with allure.step('Отправить DELETE-запрос на удаление курьера без id'):
            response = requests.delete(Urls.DELETE_COURIER_URL)
        
        assert response.status_code == 400, (
            f'Получен статус-код {response.status_code}, '
            f'ожидался 400')
        assert response.json()['message'] == Messages.DELETE_COURIER_WITHOUT_ID, (
            f'Получено сообщение "{response.json()['message']}", '
            f'ожидалось "{Messages.DELETE_COURIER_WITHOUT_ID}"')


    @allure.title('Ошибка, если передан несуществующий id курьера')
    def test_delete_courier_id_not_exist(self):
        with allure.step('Отправить DELETE-запрос на удаление курьера с несуществующим id'):
            response = requests.delete(f"{Urls.DELETE_COURIER_URL}99999999")
            
        assert response.status_code == 404, (
            f'Получен статус-код {response.status_code}, '
            f'ожидался 404')
        assert response.json()['message'] == Messages.DELETE_COURIER_ID_NOT_EXIST, (
            f'Получено сообщение "{response.json()['message']}", '
            f'ожидалось "{Messages.DELETE_COURIER_ID_NOT_EXIST}"')