import allure
import requests

from data import Urls


@allure.feature('Получение списка заказов')
class TestOrderList:
    
    @allure.title('Запрос на получение списка заказов возвращает список')
    def test_get_orders_returns_list(self):
        with allure.step('Отправить GET-запрос на получение списка заказов'):
            response = requests.get(Urls.GET_ORDERS_URL)
        
        assert response.status_code == 200, (
        f'Получен статус-код {response.status_code}, ожидался 200 OK')

        assert isinstance(response.json().get("orders"), list), (
        f'В ответе нет списка "orders". Получен ответ: {response.json()}')
