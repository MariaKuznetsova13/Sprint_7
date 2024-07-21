import allure
import pytest
import requests
import helpers
from data import ResponsesText
from data import Urls


class TestLoginCourier:
    @allure.title('Логин курьера')
    @allure.description('Проверяем, что курьер авторизуется, если переданы обязательные поля и успешный запрос возвращает id')
    def test_login_courier(self, courier):
        create_response = requests.post(Urls.CREATE_COURIER_URL, json=courier)
        if create_response.status_code == 201:
            register_data = helpers.create_register_data(courier)
            login_response = requests.post(Urls.LOGIN_COURIER_URL, json=register_data)
            assert login_response.status_code == 200 and "id" in login_response.json()

    @allure.title('Логин курьера с некорректным паролем или логином')
    @allure.description('Проверяем, что при логине с некорректным паролем или логином возвращается ошибка')
    @pytest.mark.parametrize("login_type", ["password", "login"])
    def test_login_with_wrong_credentials(self, courier, login_type):
        create_response = requests.post(Urls.CREATE_COURIER_URL, json=courier)
        if create_response.status_code == 201:
            register_data = helpers.create_register_data(courier)
            if login_type == "password":
                register_data['password'] = register_data['login']
            else:
                register_data['login'] = register_data['password']
            login_response = requests.post(Urls.LOGIN_COURIER_URL, json=register_data)
            assert login_response.status_code == 404 and login_response.json()[
                'message'] == ResponsesText.LOGIN_WITH_WRONG_PASSWORD_OR_LOGIN

    @allure.title('Логин курьера без логина или пароля')
    @allure.description('Проверяем, что при логине курьера без логина или пароля возвращается ошибка')
    @pytest.mark.parametrize('login_type', ['login', 'password'])
    def test_login_without_credentials(self, courier, login_type):
        create_response = requests.post(Urls.CREATE_COURIER_URL, json=courier)
        if create_response.status_code == 201:
            register_data = helpers.create_register_data(courier)
            register_data[login_type] = ''
            login_response = requests.post(Urls.LOGIN_COURIER_URL, json=register_data)
            assert login_response.status_code == 400 and login_response.json()[
                'message'] == ResponsesText.LOGIN_WITHOUT_PASSWORD_OR_LOGIN

    @allure.title('Логин несуществующего пользователя')
    @allure.description('Проверяем, что если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_non_existent_user(self, courier):
        register_data = helpers.create_register_data(courier)
        login_response = requests.post(Urls.LOGIN_COURIER_URL, json=register_data)
        assert login_response.status_code == 404 and login_response.json()['message'] == ResponsesText.NON_EXISTENT_USER
