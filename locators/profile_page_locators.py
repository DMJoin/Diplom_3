from selenium.webdriver.common.by import By

class ProfilePageLocators:
    ACCOUNT_HEADER = (By.XPATH, "//a[text() = 'Профиль']")  
    HISTORY_ORDER_BUTTON = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")
    
   
    