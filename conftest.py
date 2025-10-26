import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


class Config:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/"
    BROWSER = "firefox"
    TIMEOUT = 10

@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания и закрытия браузера"""
    # Используем системный Firefox драйвер
    service = Service()
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(10)
    driver.get(Config.BASE_URL)
    
    yield driver
    
    driver.quit()

@pytest.fixture
def main_page(driver):
    from pages.main_page import MainPage
    return MainPage(driver)

@pytest.fixture
def order_page(driver):
    from pages.order_page import OrderPage
    return OrderPage(driver)