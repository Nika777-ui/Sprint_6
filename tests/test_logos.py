import pytest
import allure
from pages.main_page import MainPage


@allure.feature('Проверка логотипов')
class TestLogos:
    
    @allure.title('Проверка логотипа Самоката')
    def test_scooter_logo_redirect(self, driver):
        """Проверяем что логотип Самоката ведет на главную страницу"""
        main_page = MainPage(driver)
        
        with allure.step('Нажимаем на логотип Самоката'):
            main_page.click_scooter_logo()
        
        with allure.step('Проверяем что открылась главная страница'):
            main_page.wait_for_url("https://qa-scooter.praktikum-services.ru/")
            
            current_url = main_page.get_current_url()
            assert current_url == "https://qa-scooter.praktikum-services.ru/", \
                f"Ожидался URL главной страницы, получен: {current_url}"

    @allure.title('Проверка логотипа Яндекса')
    def test_yandex_logo_redirect(self, driver):
        """Проверяем что логотип Яндекса открывает Дзен в новом окне"""
        main_page = MainPage(driver)
        
        with allure.step('Нажимаем на логотип Яндекса'):
            main_page.click_yandex_logo()
        
        with allure.step('Проверяем что открылся Дзен'):
            main_page.switch_to_new_window()
            main_page.wait_for_url_contains("dzen.ru")
            
            current_url = main_page.get_current_url()
            assert "dzen.ru" in current_url, \
                f"Ожидался URL Дзена, получен: {current_url}"