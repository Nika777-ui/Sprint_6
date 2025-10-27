import pytest
import allure
from tests.test_data import ORDER_TEST_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage

@allure.feature('Заказ самоката')
class TestOrderFlow:

    @allure.title('Заказ через верхнюю кнопку - {data[name]} {data[last_name]}')
    @pytest.mark.parametrize('data', [ORDER_TEST_DATA[0]])
    def test_order_scooter_through_top_button(self, driver, data):
        """Заказ через верхнюю кнопку"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.click_order_button_top()
        self._complete_order_flow(order_page, data)

    @allure.title('Заказ через нижнюю кнопку - {data[name]} {data[last_name]}')
    @pytest.mark.parametrize('data', [ORDER_TEST_DATA[1]])
    def test_order_scooter_through_bottom_button(self, driver, data):
        """Заказ через нижнюю кнопку"""
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.scroll_to_bottom_order_button()
        main_page.click_order_button_bottom()
        self._complete_order_flow(order_page, data)

    def _complete_order_flow(self, order_page, data):
        """Общая логика завершения заказа"""
        order_page.fill_first_step_form(
            name=data['name'],
            last_name=data['last_name'],
            address=data['address'],
            station=data['station'],
            phone=data['phone']
        )
        
        order_page.fill_second_step_form(
            rental_period=data['rental_period'],
            color=data['color'],
            comment=data['comment']
        )
        
        success_text = order_page.confirm_order()
        assert "Заказ оформлен" in success_text