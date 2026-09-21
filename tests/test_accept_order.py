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


    @allure.title('Ошибка, если не передан id курьера')
    def test_accept_order_without_courier_id(self, created_and_cleanup_order):
        track = created_and_cleanup_order

        with allure.step('Получить id заказа по track'):
            order_id = get_order_id_by_track(track)

        with allure.step('Отправить PUT-запрос на принятие заказа без courierId'):
            response = requests.put(f"{Urls.ACCEPT_ORDER_URL}{order_id}")

        assert response.status_code == 400, (
            f'Получен статус-код {response.status_code}, '
            f'ожидался 400')
        
        assert response.json()["message"] == Messages.ACCEPT_ORDER_WITHOUT_COURIER_ID, (
            f'Получено сообщение {response.json()["message"]}, '
            f'ожидалось {Messages.ACCEPT_ORDER_WITHOUT_COURIER_ID}')


    @allure.title('Ошибка, если передан несуществующий id курьера')
    def test_accept_order_with_wrong_courier_id(self, created_and_cleanup_order):
        track = created_and_cleanup_order

        with allure.step('Получить id заказа по track'):
            order_id = get_order_id_by_track(track)

        with allure.step('Отправить PUT-запрос с несуществующим courierId'):
            response = requests.put(f"{Urls.ACCEPT_ORDER_URL}{order_id}", params={'courierId': 999999999})

        assert response.status_code == 404, (
            f'Получен статус-код {response.status_code}, '
            f'ожидался 404')
        
        assert response.json()["message"] == Messages.ACCEPT_ORDER_COURIER_ID_NOT_EXIST, (
            f'Получено сообщение {response.json()["message"]}, '
            f'ожидалось {Messages.ACCEPT_ORDER_COURIER_ID_NOT_EXIST}')


    @allure.title('Ошибка, если не передан id заказа')
    def test_accept_order_without_order_id(self, create_and_delete_courier):
        courier = create_and_delete_courier

        with allure.step('Получить id курьера'):
            courier_id = get_courier_id(courier["login"], courier["password"])

        with allure.step('Отправить PUT-запрос на принятие заказа без id'):
            response = requests.put(Urls.ACCEPT_ORDER_URL, params={'courierId': courier_id})

        assert response.status_code == 400, (
            f'Получен статус-код {response.status_code}, '
            f'ожидался 400')
        
        assert response.json()["message"] == Messages.ACCEPT_ORDER_WITHOUT_ORDER_ID, (
            f'Получено сообщение {response.json()["message"]}, '
            f'ожидалось {Messages.ACCEPT_ORDER_WITHOUT_ORDER_ID}')
        

    @allure.title('Ошибка, если передан несуществующий id заказа')
    def test_accept_order_with_wrong_order_id(self, create_and_delete_courier):
        courier = create_and_delete_courier

        with allure.step('Получить id курьера'):
            courier_id = get_courier_id(courier["login"], courier["password"])

        with allure.step('Отправить PUT-запрос с несуществующим id заказа'):
            response = requests.put(f"{Urls.ACCEPT_ORDER_URL}999999999", params={'courierId': courier_id})

        assert response.status_code == 404, (
            f'Получен статус-код {response.status_code}, '
            f'ожидался 404')
        
        assert response.json()["message"] == Messages.ACCEPT_ORDER_ORDER_ID_NOT_EXIST, (
            f'Получено сообщение {response.json()["message"]}, '
            f'ожидалось {Messages.ACCEPT_ORDER_ORDER_ID_NOT_EXIST}')