import requests
import allure

from data import Urls, Messages
from generators import generate_order_data


@allure.feature('Получение заказа по трекинговому номеру')
class TestGetOrderByTrack:

    @allure.title('Успешное получение заказа по номеру track')
    def test_get_order_by_track(self, created_and_cleanup_order):
        with allure.step('Отправить запрос на получение заказа по track'):
            response = requests.get(Urls.GET_ORDER_BY_TRACK_URL, params={'t': created_and_cleanup_order})

        assert response.status_code == 200, (
            f'Получен статус-код {response.status_code}, ожидался 200.')
        assert 'order' in response.json(), (
            f'Ответ не содержит объект "order". Тело ответа: {response.json()}')


    @allure.title('Ошибка при отправке запроса на получение заказа без номера')
    def test_get_order_without_track(self):
        with allure.step('Отправить запрос на получение заказа без track'):
            response = requests.get(Urls.GET_ORDER_BY_TRACK_URL)
    
        assert response.status_code == 400, (
            f'Получен статус-код {response.status_code}, ожидался 400.')
        
        assert response.json()['message'] == Messages.GET_ORDER_WITHOUT_TRACK, (
            f'Получен ответ {response.json()}, '
            f'ожидался {Messages.GET_ORDER_WITHOUT_TRACK}')


    @allure.title('Ошибка при отправке запроса на получение заказа с несуществующим номером')
    def test_get_order_track_not_exist(self):
        with allure.step('Отправить запрос на получение заказа с track = 1'):
            response = requests.get(Urls.GET_ORDER_BY_TRACK_URL, params={'t': 1})
    
        assert response.status_code == 404, (
            f'Получен статус-код {response.status_code}, ожидался 404.')
        
        assert response.json()['message'] == Messages.GET_ORDER_TRACK_NOT_EXIST, (
            f'Получен ответ {response.json()}, '
            f'ожидался {Messages.GET_ORDER_TRACK_NOT_EXIST}')