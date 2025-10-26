from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import time

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @property
    def locators(self):
        """Доступ к локаторам"""
        return MainPageLocators
    
    def scroll_to_faq_section(self):
        """Прокрутить страницу к разделу FAQ"""
        self.scroll_to_element(self.locators.FAQ_QUESTION_1)
        time.sleep(1)
    
    def scroll_to_bottom_order_button(self):
        """Прокрутить страницу к нижней кнопке 'Заказать'"""
        self.scroll_to_element(self.locators.ORDER_BUTTON_BOTTOM)
        time.sleep(1)
    
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
        time.sleep(1)
    
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
    
    def click_order_button_top(self):
        """Клик по верхней кнопке 'Заказать'"""
        self.click_element(self.locators.ORDER_BUTTON_TOP)
    
    def click_order_button_bottom(self):
        """Клик по нижней кнопке 'Заказать'"""
        self.click_element(self.locators.ORDER_BUTTON_BOTTOM)

def click_scooter_logo(self):
    """Клик по логотипу Самоката"""
    self.click_element(self.locators.SCOOTER_LOGO)

def click_yandex_logo(self):
    """Клик по логотипу Яндекса"""
    self.click_element(self.locators.YANDEX_LOGO)       