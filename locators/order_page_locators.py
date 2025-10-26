from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Первая страница
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO_STATION = (By.XPATH, "//input[@class='select-search__input']")
    
    # ← ФИНАЛЬНЫЙ ЛОКАТОР: точный текст
    METRO_STATION_OPTION = lambda station: (
        By.XPATH, f"//li[contains(@class, 'select-search__row')]//div[text()='{station}']"
    )
    
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")

    # Вторая страница
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DATE_OPTION = lambda day: (
        By.XPATH, f"//div[contains(@class, 'react-datepicker__day') and text()='{day}' and not(contains(@class, 'outside'))]"
    )
    
    # Срок аренды:
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_PERIOD_OPTION = lambda period: (
        By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period}']"
    )
    
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    INPUT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BUTTON_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    # Модальные окна
    CONFIRMATION_MODAL = (By.XPATH, "//div[contains(text(), 'Хотите оформить заказ')]")
    BUTTON_YES = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")