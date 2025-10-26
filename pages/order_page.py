from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from datetime import datetime, timedelta


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_first_step_form(self, name, last_name, address, station, phone):
        self.input_text(OrderPageLocators.INPUT_NAME, name)
        self.input_text(OrderPageLocators.INPUT_LAST_NAME, last_name)
        self.input_text(OrderPageLocators.INPUT_ADDRESS, address)

        print(f"Выбираем станцию: {station}...")
        metro_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.INPUT_METRO_STATION)
        )
        metro_input.click()
        metro_input.clear()
        metro_input.send_keys(station[:3])
        
        option_locator = OrderPageLocators.METRO_STATION_OPTION(station)
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(option_locator)
        )
        option.click()
        print(f"Выбрана: {station}")

        self.input_text(OrderPageLocators.INPUT_PHONE, phone)
        self.click_element(OrderPageLocators.BUTTON_NEXT)

    def fill_second_step_form(self, rental_period="сутки", color="black", comment=""):
        # Дата
        tomorrow = (datetime.now() + timedelta(days=1)).day
        self.click_element(OrderPageLocators.INPUT_DATE)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.DATE_OPTION(tomorrow))
        ).click()

        # Срок аренды
        print(f"Выбираем срок аренды: {rental_period}...")
        field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD)
        )
        field.click()
        
        option_locator = OrderPageLocators.RENTAL_PERIOD_OPTION(rental_period)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(option_locator)
        ).click()

        # Цвет
        if color == "black":
            self.click_element(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click_element(OrderPageLocators.COLOR_GREY)

        # Комментарий
        if comment:
            self.input_text(OrderPageLocators.INPUT_COMMENT, comment)

        # Кнопка Заказать
        print("Нажимаем кнопку 'Заказать'...")
        order_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.BUTTON_ORDER)
        )
        print(f"Кнопка найдена: {order_btn.text}")
        order_btn.click()

    def confirm_order(self):
        """Подтверждение заказа в модальном окне"""
        print("Ожидаем модальное окно подтверждения...")
        confirmation_modal = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.CONFIRMATION_MODAL)
        )
        print(f"Модальное окно: {confirmation_modal.text}")
        
        print("Нажимаем 'Да'...")
        yes_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.BUTTON_YES)
        )
        yes_btn.click()
        
        print("Ожидаем окно успеха...")
        success_modal = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MODAL)
        )
        success_text = success_modal.text
        print(f"Успех: {success_text}")
        return success_text