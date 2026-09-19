import pytest

from generators import generate_random_string
from helpers import register_new_courier, get_courier_id, delete_courier


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