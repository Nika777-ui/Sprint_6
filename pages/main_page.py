from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class MainPage(BasePage):
    @property
    def locators(self):
        """Доступ к локаторам"""
        return MainPageLocators
    
    @allure.step("Прокрутить к разделу FAQ")
    def scroll_to_faq_section(self):
        """Прокрутить страницу к разделу FAQ"""
        self.scroll_to_element(self.locators.FAQ_QUESTION_1)
    
    @allure.step("Прокрутить к нижней кнопке 'Заказать'")
    def scroll_to_bottom_order_button(self):
        """Прокрутить страницу к нижней кнопке 'Заказать'"""
        self.scroll_to_element(self.locators.ORDER_BUTTON_BOTTOM)
    
    @allure.step("Клик по вопросу в FAQ №{question_number}")
    def click_faq_question(self, question_number):
        """Клик по вопросу в FAQ"""
        faq_locators = {
            1: MainPageLocators.FAQ_QUESTION_1,
            2: MainPageLocators.FAQ_QUESTION_2,
            3: MainPageLocators.FAQ_QUESTION_3,
            4: MainPageLocators.FAQ_QUESTION_4,
            5: MainPageLocators.FAQ_QUESTION_5,
            6: MainPageLocators.FAQ_QUESTION_6,
            7: MainPageLocators.FAQ_QUESTION_7,
            8: MainPageLocators.FAQ_QUESTION_8
        }
        
        locator = faq_locators[question_number]
        self.click_element(locator)
    
    @allure.step("Получить текст ответа из FAQ №{answer_number}")
    def get_faq_answer_text(self, answer_number):
        """Получить текст ответа из FAQ"""
        answer_locators = {
            1: MainPageLocators.FAQ_ANSWER_1,
            2: MainPageLocators.FAQ_ANSWER_2,
            3: MainPageLocators.FAQ_ANSWER_3,
            4: MainPageLocators.FAQ_ANSWER_4,
            5: MainPageLocators.FAQ_ANSWER_5,
            6: MainPageLocators.FAQ_ANSWER_6,
            7: MainPageLocators.FAQ_ANSWER_7,
            8: MainPageLocators.FAQ_ANSWER_8
        }
        
        locator = answer_locators[answer_number]
        element = self.wait_for_element_visible(locator)
        return element.text
    
    @allure.step("Клик по верхней кнопке 'Заказать'")
    def click_order_button_top(self):
        """Клик по верхней кнопке 'Заказать'"""
        self.click_element(self.locators.ORDER_BUTTON_TOP)
    
    @allure.step("Клик по нижней кнопке 'Заказать'")
    def click_order_button_bottom(self):
        """Клик по нижней кнопке 'Заказать'"""
        self.click_element(self.locators.ORDER_BUTTON_BOTTOM)

    @allure.step("Клик по логотипу Самоката")
    def click_scooter_logo(self):
        """Клик по логотипу Самоката"""
        self.click_element(self.locators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        """Клик по логотипу Яндекса"""
        self.click_element(self.locators.YANDEX_LOGO)       