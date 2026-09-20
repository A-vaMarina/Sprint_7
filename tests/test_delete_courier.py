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

