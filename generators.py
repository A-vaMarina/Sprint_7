import datetime
import random
import string

from faker import Faker

fake = Faker('ru_RU')

def generate_random_string(length=10):
# генерация строки, состоящей только из букв нижнего регистра, в качестве параметра передаём длину строки
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_order_data():
# генерация данных для создания заказа самоката
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": 1,
        "phone": fake.phone_number(),
        "rentTime": 2,
        "deliveryDate": str(datetime.date.today() + datetime.timedelta(days=2)),
        "comment": fake.text(max_nb_chars=30)
    }