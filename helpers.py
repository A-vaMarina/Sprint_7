import requests

from data import Urls
from generators import generate_random_string


def register_new_courier():
    """
    Регистрация нового курьера со случайными данными.
    Возвращает словарь {'login', 'password', 'firstName'} или None, если регистрация не удалась.
    """
    payload = {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string(),
    }
    
    response = requests.post(Urls.CREATE_COURIER_URL, data=payload)
    
    if response.status_code == 201:
        return payload        
    return None


def get_courier_id(login, password):
    """
    Логинит курьера и возвращает его id.
    Возвращает None, если логин не удался.
    """
    payload = {"login": login, "password": password}
    response = requests.post(Urls.LOGIN_COURIER_URL, data=payload)

    if response.status_code == 200:
        return response.json().get("id")
    return None


def delete_courier(courier_id):
    """
    Удаляет курьера по его id. Возвращает response.
    """
    return requests.delete(f"{Urls.DELETE_COURIER_URL}{courier_id}")


def cancel_order(track):
    return requests.put(Urls.CANCEL_ORDER_URL, params={'track': track})    


def create_order(payload):
    return requests.post(Urls.CREATE_ORDER_URL, json=payload)


def get_order_id_by_track(track):
    """
    Получает id заказа из ответа на запрос на получение заказа по его track-номеру.
    """
    response = requests.get(Urls.GET_ORDER_BY_TRACK_URL, params={'t': track})
    return response.json()['order']['id']