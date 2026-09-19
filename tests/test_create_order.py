import requests
import allure
import pytest

from data import Urls
from generators import generate_order_data


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Успешное создание заказа и получение его трекингового номера')
    @pytest.mark.parametrize("colors", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        [],
    ])
    def test_create_order(self, colors):
        with allure.step('Создание заказа с разными цветами'):
            payload = generate_order_data()
            payload["color"] = colors

        response = requests.post(Urls.CREATE_ORDER_URL, json=payload)

        assert response.status_code == 201, (
                f'Получен статус-код {response.status_code}, '
                f'ожидался 201 Created')
        assert 'track' in response.json(), (f'В ответе нет ключа "track". Получен ответ: {response.json()}')
