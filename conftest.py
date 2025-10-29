import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope="function")
def driver():
    """Фикстура для создания и закрытия браузера"""
    service = Service()
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(10)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()