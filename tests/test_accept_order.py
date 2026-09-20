import requests
import allure

from data import Urls, Messages
from helpers import get_courier_id, get_order_id_by_track


@allure.feature('Принять заказ')
class TestAcceptOrder:

    @allure.title('Успешное принятие заказа')
    def test_accept_order_with_couier_id_and_order_id(self, create_and_delete_courier, created_and_cleanup_order):

        courier = create_and_delete_courier
        track = created_and_cleanup_order

        with allure.step('Получить id курьера'):
            courier_id = get_courier_id(courier["login"], courier["password"])

        with allure.step('Получить id заказа по track'):
            order_id = get_order_id_by_track(track)

        with allure.step('Отправить PUT-запрос на принятие заказа'):
            response = requests.put(f"{Urls.ACCEPT_ORDER_URL}{order_id}", params={'courierId': courier_id})

        assert response.status_code == 200, (
            f'Получен статус-код {response.status_code}, '
            f'ожидался 200')
        assert response.json() == Messages.ACCEPT_ORDER_SUCCESS, (
            f'Получен ответ {response.json()}, '
            f'ожидался {Messages.ACCEPT_ORDER_SUCCESS}')