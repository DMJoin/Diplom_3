import allure
from pages.base_page import BasePage
from locators.login_page_locators import *


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание загрузки заголовка Вход')
    def wait_login_page_for_load(self):
        self.find_element(LoginPageLocators.AUTH_HEADER)

    @allure.step('Клик на кнопку Войти')
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Клик на кнопку Восстановить пароль')
    def click_password_recovery_button(self):
        self.click_element(LoginPageLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Ввести email')
    def enter_email(self, email):
        self.text_input(LoginPageLocators.EMAIL_FIELD, email)

    @allure.step('Ввести password')
    def enter_password(self, password):
        self.text_input(LoginPageLocators.PASSWORD_FIELD, password)
