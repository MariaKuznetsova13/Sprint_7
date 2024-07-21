import requests
import random
import string
from data import Urls


def register_new_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    credentials = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return credentials


def create_register_data(credentials):
    return {
        'login': credentials['login'],
        'password': credentials['password']
    }


def login_courier(credentials):
    register_data = create_register_data(credentials)
    login_response = requests.post(Urls.LOGIN_COURIER_URL, data=register_data)
    courier_id = login_response.json().get('id')
    return courier_id


def delete_courier(credentials):
    courier_id = login_courier(credentials)
    response = requests.delete(Urls.DELETE_COURIER_URL + str(courier_id))
    return response