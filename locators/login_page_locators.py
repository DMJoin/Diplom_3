from selenium.webdriver.common.by import By

class LoginPageLocators:
    AUTH_HEADER = (By.XPATH, "//h2[text()='Вход']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    