from selenium.webdriver.common.by import By

class RecoveryPasswordLocators:
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")  
    RECOVER_PASSWORD_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    PASSWORD_FIELD_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")
    CODE_INPUT = (By.XPATH, "//label[text()='Введите код из письма']")
    
    
    