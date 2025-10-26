import pytest
import allure
from tests.test_data import ORDER_TEST_DATA


@allure.feature('Заказ самоката')
class TestOrderFlow:

    @allure.title('Позитивный сценарий заказа самоката через {data[button]} кнопку')
    @pytest.mark.parametrize('data', ORDER_TEST_DATA)
    def test_order_scooter_positive_flow(self, driver, main_page, order_page, data):
        with allure.step(f'Нажимаем {data["button"]} кнопку "Заказать"'):
            if data['button'] == 'верхнюю':
                main_page.click_order_button_top()
            else:
                main_page.scroll_to_bottom_order_button()
                main_page.click_order_button_bottom()

        with allure.step('Заполняем первую страницу формы заказа'):
            order_page.fill_first_step_form(
                name=data['name'],
                last_name=data['last_name'],
                address=data['address'],
                station=data['station'],
                phone=data['phone']
            )

        with allure.step('Заполняем вторую страницу формы заказа'):
            order_page.fill_second_step_form(
                rental_period=data['rental_period'],
                color=data['color'],
                comment=data['comment']
            )

        with allure.step('Подтверждаем заказ'):
            success_text = order_page.confirm_order()
            assert "Заказ оформлен" in success_text

        print(f"Успешный заказ через {data['button']} кнопку!")