import random
import string


def generate_random_string(length=10):
# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string
