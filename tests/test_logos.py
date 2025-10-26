import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature('Проверка логотипов')
class TestLogos:
    
    @allure.title('Проверка логотипа Самоката')
    def test_scooter_logo_redirect(self, driver, main_page):
        """Проверяем что логотип Самоката ведет на главную страницу"""
        with allure.step('Нажимаем на логотип Самоката'):
            main_page.click_element(main_page.locators.SCOOTER_LOGO)
        
        with allure.step('Проверяем что открылась главная страница'):
            # Ждем загрузки страницы
            WebDriverWait(driver, 10).until(
                EC.url_to_be("https://qa-scooter.praktikum-services.ru/")
            )
            current_url = driver.current_url
            assert current_url == "https://qa-scooter.praktikum-services.ru/", \
                f"Ожидался URL главной страницы, получен: {current_url}"
            print("Успешный переход на главную страницу Самоката!")

    @allure.title('Проверка логотипа Яндекса')
    def test_yandex_logo_redirect(self, driver, main_page):
        """Проверяем что логотип Яндекса открывает Дзен в новом окне"""
        with allure.step('Запоминаем текущее окно'):
            original_window = driver.current_window_handle
        
        with allure.step('Нажимаем на логотип Яндекса'):
            main_page.click_element(main_page.locators.YANDEX_LOGO)
        
        with allure.step('Ждем открытия нового окна'):
            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
            
            # Переключаемся на новое окно
            for window_handle in driver.window_handles:
                if window_handle != original_window:
                    driver.switch_to.window(window_handle)
                    break
        
        with allure.step('Проверяем что открылся Дзен'):
            WebDriverWait(driver, 10).until(
                EC.url_contains("dzen.ru")
            )
            current_url = driver.current_url
            assert "dzen.ru" in current_url, \
                f"Ожидался URL Дзена, получен: {current_url}"
            print("Успешное открытие Дзена в новом окне!")
            
        with allure.step('Закрываем новое окно и возвращаемся'):
            driver.close()
            driver.switch_to.window(original_window)