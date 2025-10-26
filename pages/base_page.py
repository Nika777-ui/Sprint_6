from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        """Клик через JavaScript чтобы обойти перекрывающие элементы"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def click_element_standard(self, locator):
        """Обычный клик"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_current_url(self):
        return self.driver.current_url

    def scroll_to_element(self, locator):
        """Прокрутить страницу к элементу"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        
      