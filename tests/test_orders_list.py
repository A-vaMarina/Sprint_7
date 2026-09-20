import allure
import requests

from data import Urls


@allure.feature('Получение списка заказов')
class TestOrderList:
    
    @allure.title('Запрос на получение списка заказов возвращает список')
    def test_get_orders_returns_list(self):
        payload = {
            'nearestStation': '["1", "2"]',
            'limit': 5,
            'page': 0
        }

        with allure.step('Отправить GET-запрос на получение списка заказов'):
            response = requests.get(Urls.GET_ORDERS_URL, params=payload)

        body = response.json()
        
        assert response.status_code == 200, (
        f'Получен статус-код {response.status_code}, ожидался 200 OK')

        assert "orders" in body, (f'Ответ не содержит объект "orders". Ответ: {body}')

        assert isinstance(body['orders'], list), (
        f'В ответе "orders" не список. Получен ответ: {body}. Тип: {type(body["orders"])}')
