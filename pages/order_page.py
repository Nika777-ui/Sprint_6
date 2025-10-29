from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from datetime import datetime, timedelta
import allure


class OrderPage(BasePage):
    
    @allure.step("Заполнить первую страницу формы заказа")
    def fill_first_step_form(self, name, last_name, address, station, phone):
        self.input_text(OrderPageLocators.INPUT_NAME, name)
        self.input_text(OrderPageLocators.INPUT_LAST_NAME, last_name)
        self.input_text(OrderPageLocators.INPUT_ADDRESS, address)

        with allure.step(f"Выбрать станцию метро: {station}"):
            # Используем методы BasePage
            metro_input = self.wait_for_element_visible(OrderPageLocators.INPUT_METRO_STATION)
            metro_input.click()
            metro_input.clear()
            metro_input.send_keys(station[:3])
            
            option_locator = OrderPageLocators.METRO_STATION_OPTION(station)
            option = self.wait_for_element_clickable(option_locator)
            option.click()

        self.input_text(OrderPageLocators.INPUT_PHONE, phone)
        self.click_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step("Заполнить вторую страницу формы заказа")
    def fill_second_step_form(self, rental_period="сутки", color="black", comment=""):
        # Дата
        tomorrow = (datetime.now() + timedelta(days=1)).day
        self.click_element(OrderPageLocators.INPUT_DATE)
        self.wait_for_element_clickable(OrderPageLocators.DATE_OPTION(tomorrow)).click()

        # Срок аренды
        with allure.step(f"Выбрать срок аренды: {rental_period}"):
            field = self.wait_for_element_clickable(OrderPageLocators.RENTAL_PERIOD)
            field.click()
            
            option_locator = OrderPageLocators.RENTAL_PERIOD_OPTION(rental_period)
            self.wait_for_element_clickable(option_locator).click()

        # Цвет
        if color == "black":
            self.click_element(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click_element(OrderPageLocators.COLOR_GREY)

        # Комментарий
        if comment:
            self.input_text(OrderPageLocators.INPUT_COMMENT, comment)

        # Кнопка Заказать
        with allure.step("Нажать кнопку 'Заказать'"):
            order_btn = self.wait_for_element_clickable(OrderPageLocators.BUTTON_ORDER)
            order_btn.click()

    @allure.step("Подтвердить заказ в модальном окне")
    def confirm_order(self):
        """Подтверждение заказа в модальном окне"""
        confirmation_modal = self.wait_for_element_visible(OrderPageLocators.CONFIRMATION_MODAL)
        
        yes_btn = self.wait_for_element_clickable(OrderPageLocators.BUTTON_YES)
        yes_btn.click()
        
        success_modal = self.wait_for_element_visible(OrderPageLocators.SUCCESS_MODAL)
        return success_modal.text