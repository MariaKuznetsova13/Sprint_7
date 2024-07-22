import allure
import pytest
import requests
from data import Urls
from data import OrderInfo


class TestCreateOrder:
    @allure.title('Создание заказа')
    @allure.description('Проверяем, что можно создать заказ с разными данные в поле "color"')
    @pytest.mark.parametrize(
        'order_info',
        [
            OrderInfo.ORDER_INFO_BLACK_COLOR,
            OrderInfo.ORDER_INFO_GREY_COLOR,
            OrderInfo.ORDER_INFO_BLACK_AND_GREY_COLOR,
            OrderInfo.ORDER_INFO_WITHOUT_COLOR
        ]
    )
    def test_create_order(self, order_info):
        create_order_response = requests.post(Urls.CREATE_ORDER_URL, json=order_info)
        assert create_order_response.status_code == 201 and 'track' in create_order_response.json()
