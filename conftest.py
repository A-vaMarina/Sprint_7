import pytest

from generators import generate_order_data
from helpers import register_new_courier, get_courier_id, delete_courier, cancel_order, create_order


@pytest.fixture
def cleanup_courier():
    """
    Постусловие для тестов на создание курьера.
    Тест сам создаёт курьера и кладёт его данные в словарь.
    После теста фикстура логинит курьера и удаляет его по id.
    Если тест не успел создать курьера — фикстура ничего не делает.
    """
    courier = {}

    yield courier

    if courier:
        courier_id = get_courier_id(courier["login"], courier["password"])
        if courier_id is not None:
            delete_courier(courier_id)


@pytest.fixture
def create_and_delete_courier():
    """
    Пред- и постусловие для тестов на логин (и других, где курьер нужен заранее).
    Создаёт курьера до теста, удаляет после.
    Возвращает словарь с данными курьера.
    """
    courier = register_new_courier()

    yield courier

    if courier:
        courier_id = get_courier_id(courier["login"], courier["password"])
        if courier_id is not None:
            delete_courier(courier_id)


@pytest.fixture
def cleanup_orders():
    """
    Постусловие для тестов на создание заказа.
    Тест передает трек-номер заказа, фикстура отменяет заказ по треку после теста.
    """
    tracks = []

    yield tracks

    for track in tracks:
        cancel_order(track)


@pytest.fixture
def created_and_cleanup_order():
    """
    Пред- и постусловие для тестов, где нужет созданный заказ.
    Создаёт заказ, передаёт track в тест, после теста отменяет заказ.
    """
    payload = generate_order_data()
    response = create_order(payload)
    track = response.json()['track']

    yield track

    cancel_order(track)