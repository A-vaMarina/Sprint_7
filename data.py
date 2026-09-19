class Urls:

    BASE_URL = 'https://qa-scooter.praktikum-services.ru'

    CREATE_COURIER_URL = f'{BASE_URL}/api/v1/courier'  # POST - создание курьера
    LOGIN_COURIER_URL = f'{BASE_URL}/api/v1/courier/login' # POST - логин курьера в системе
    DELETE_COURIER_URL = f'{BASE_URL}/api/v1/courier/' # DELETE - удаление курьера

    CREATE_ORDER_URL = f'{BASE_URL}/api/v1/orders' # POST - создание заказа
    GET_ORDERS_URL = f'{BASE_URL}/api/v1/orders' # GET - получение списка заказов
    ACCEPT_ORDER_URL = f'{BASE_URL}/api/v1/orders/accept/' # PUT - принять заказ
    GET_ORDER_BY_TRACK_URL = f'{BASE_URL}/api/v1/orders/track' # GET - получить заказ по его номеру
    CANCEL_ORDER_URL  = f'{BASE_URL}/api/v1/orders' # PUT - отменить заказ

class Messages:

    # POST /api/v1/courier - создание курьера
    # Успешное создание курьера
    CREATE_COURIER_SUCCESS = {"ok": True}  # 201 Created
    # Сообщения об ошибке при создании курьера
    CREATE_COURIER_MISSING_FIELDS = "Недостаточно данных для создания учетной записи"  # 400 Bad Request
    CREATE_COURIER_ALREADY_EXISTS = "Этот логин уже используется"  # 409 Сonflict

    # POST /api/v1/courier/login - логин курьера
    # Сообщения об ошибке при логине курьера
    LOGIN_COURIER_MISSING_FIELDS = "Недостаточно данных для входа"  # 400 Bad Request
    LOGIN_COURIER_NOT_FOUND = "Учетная запись не найдена"  # 404 Not Found

    # DELETE /api/v1/courier/:id - удаление курьера
    # Успешное удаление курьера
    DELETE_COURIER_SUCCESS = {"ok": True}  # 200 OK
    # Сообщения об ошибке при удалении курьера
    DELETE_COURIER_WITHOUT_ID = "Недостаточно данных для удаления курьера"  # 400 Bad Request
    DELETE_COURIER_ID_NOT_EXIST = "Курьера с таким id нет" #  404 Not Found

    # PUT /api/v1/orders/accept/:id - принять заказ
    # Заказ принят успешно
    ACCEPT_ORDER_SUCCESS = {"ok": True}  # 200
    # Сообщения об ошибке при принятии заказа
    ACCEPT_ORDER_WITHOUT_COURIER_ID = "Недостаточно данных для поиска"  # 400 Conflict
    ACCEPT_ORDER_COURIER_ID_NOT_EXIST = "Курьера с таким id не существует"  # 404 Not Found
    ACCEPT_ORDER_WITHOUT_ORDER_ID = "Недостаточно данных для поиска"  # 400 Bad Request
    ACCEPT_ORDER_ORDER_ID_NOT_EXIST = "Заказа с таким id не существует"  # 404 Not Found

    # GET /api/v1/orders/track - получить заказ по его трекинговому номеру
    # Сообщения об ошибке при получении заказа по его номеру t
    GET_ORDER_WITHOUT_TRACK = "Недостаточно данных для поиска"  # 400 Bad Request
    GET_ORDER_TRACK_NOT_EXIST = "Заказ не найден"  # 404 Not Found
