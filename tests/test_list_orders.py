import allure
import requests
from data import Urls


class TestListOrders:
    @allure.title('Получение всего списка заказов')
    @allure.description('Проверяем, что в тело ответа возвращается список всех заказов')
    def test_list_orders(self):
        response_list = requests.get(Urls.GET_ORDER_LIST)
        assert response_list.status_code == 200 and isinstance(response_list.json()['orders'], list)
