# Sprint_7

# Запустить тесты для создания курьера
pytest tests/test_create_courier.py

# Запустить тесты для логина курьера
pytest tests/test_login_courier.py

# Запустить тесты для создания заказа
pytest tests/test_create_order.py

# Запустить тесты для получения списка заказов
pytest tests/test_orders_list.py

pytest tests/test_get_order.py -v


# Запустить конкретный файл с тестами в Allure
pytest tests/test_login_courier.py --alluredir=allure-results -v

# Прогнать все тесты в Allur
pytest --alluredir=allure-results -v

# Посмотреть отчет Allur
allure serve allure-results