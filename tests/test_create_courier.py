import allure
import requests
from helpers import register_new_courier
from data import ResponsesText
from data import Urls


class TestCreateCourier:
    @allure.title('Создание курьера')
    @allure.description('Проверяем создание нового курьера с обязательными параметрами')
    def test_create_courier(self, courier):
        response = requests.post(Urls.CREATE_COURIER_URL, json=courier)
        assert response.status_code == 201 and response.json()['ok'] is True

    @allure.title('Создание двух одинаковых курьеров')
    @allure.description('Проверяем, что при создании двух одинаковых курьеров возвращается ошибка')
    def test_create_dup_courier(self, courier):
        first_response = requests.post(Urls.CREATE_COURIER_URL, json=courier)
        second_response = requests.post(Urls.CREATE_COURIER_URL, json=courier)
        assert second_response.status_code == 409 and second_response.json()['message'] == ResponsesText.DUB_COURIER_MESSAGE

    @allure.title('Создание курьера без логина')
    @allure.description('Проверяем, что при создании курьера без логина возвращается ошибка')
    def test_create_courier_without_login_or_password(self):
        credentials = register_new_courier()
        del credentials['login']
        response = requests.post(Urls.CREATE_COURIER_URL, json=credentials)
        assert response.status_code == 400 and response.json()['message'] == ResponsesText.CREATE_COURIER_WITHOUT_REQUIRED_PARAMS_MESSAGE

    @allure.title('Создание курьера без пароля')
    @allure.description('Проверяем, что при создании курьера без пароля возвращается ошибка')
    def test_create_courier_without_login_or_password(self):
        credentials = register_new_courier()
        del credentials['password']
        response = requests.post(Urls.CREATE_COURIER_URL, json=credentials)
        assert response.status_code == 400 and response.json()['message'] == ResponsesText.CREATE_COURIER_WITHOUT_REQUIRED_PARAMS_MESSAGE

    @allure.title('Создание двух курьеров с одинаковым логином')
    @allure.description('Проверяем, что при создании двух курьеров с одинаковым логином возвращается ошибка')
    def test_create_courier_with_same_login(self, courier):
        first_response = requests.post(Urls.CREATE_COURIER_URL, json=courier)
        new_courier = {
                "login": courier['login'],
                "password": "1234567",
                "firstName": "Maiz"
            }
        second_response = requests.post(Urls.CREATE_COURIER_URL, json=new_courier)
        assert second_response.status_code == 409 and second_response.json()[
                'message'] == ResponsesText.DUB_COURIER_MESSAGE
