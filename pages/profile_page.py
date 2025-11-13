import allure
from pages.base_page import BasePage
from locators.profile_page_locators import *


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание загрузки страницы профиля')
    def wait_profile_page_load(self):
        self.wait_element_load(ProfilePageLocators.ACCOUNT_HEADER)

    @allure.step('Клик на кнопку История заказов')
    def click_history_order_button(self):
        self.click_element(ProfilePageLocators.HISTORY_ORDER_BUTTON)

    @allure.step('Клик на кнопку Выход из аккаунта')
    def click_logout_button(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

