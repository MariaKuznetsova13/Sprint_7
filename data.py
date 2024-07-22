class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER_URL = BASE_URL + '/api/v1/courier'
    DELETE_COURIER_URL = BASE_URL + '/api/v1/courier/{id}'
    LOGIN_COURIER_URL = BASE_URL + '/api/v1/courier/login'
    CREATE_ORDER_URL = BASE_URL + '/api/v1/orders'
    GET_ORDER_LIST = BASE_URL + '/api/v1/orders'


class ResponsesText:
    DUB_COURIER_MESSAGE = 'Этот логин уже используется. Попробуйте другой.'
    CREATE_COURIER_WITHOUT_REQUIRED_PARAMS_MESSAGE = 'Недостаточно данных для создания учетной записи'
    LOGIN_WITH_WRONG_PASSWORD_OR_LOGIN = 'Учетная запись не найдена'
    LOGIN_WITHOUT_PASSWORD_OR_LOGIN = 'Недостаточно данных для входа'
    NON_EXISTENT_USER = 'Учетная запись не найдена'


class OrderInfo:
    ORDER_INFO_BLACK_COLOR = {
        "firstName": "Narutos",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }

    ORDER_INFO_GREY_COLOR = {
        "firstName": "Narutoo",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "GREY"
        ]
    }

    ORDER_INFO_BLACK_AND_GREY_COLOR = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK",
            "GREY"
        ]
    }

    ORDER_INFO_WITHOUT_COLOR = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
        ]
    }
