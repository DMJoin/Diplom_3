import allure
from pages.base_page import BasePage
from locators.recovery_password_locators import *


class RecoveryPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик на кнопку показать пароль")
    def click_to_show_password_button(self):
        self.click_element(RecoveryPasswordLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Клик на кнопку Восстановить')
    def click_to_recovery_button(self):
        self.click_element(RecoveryPasswordLocators.RECOVERY_BUTTON)

    @allure.step("Поле пароль активно")
    def password_field_is_active(self):
        return self.find_element(RecoveryPasswordLocators.PASSWORD_FIELD_ACTIVE, 10)

    @allure.step("Ожидание загрузки Введите код из письма")
    def wait_code_input_visible(self):
        self.find_element(RecoveryPasswordLocators.CODE_INPUT, 10)

    @allure.step('Ожидание загрузки заголовка Восстановление пароля')
    def wait_recovery_password_header_visible(self):
        self.find_element(RecoveryPasswordLocators.RECOVER_PASSWORD_TITLE, 10)



    
