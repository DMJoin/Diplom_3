import allure
from pages.base_page import BasePage
from locators.main_page_locators import *


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание загрузки кнопки Войти в аккаунт')
    def wait_for_login_button_displayed(self):
        self.find_element(MainPageLocators.ENTER_BUTTON_ACCOUNT, 10)

    @allure.step('Клик на кнопку Войти в аккаунт')
    def click_login_button(self):
        self.click_element(MainPageLocators.ENTER_BUTTON_ACCOUNT)

    @allure.step('Клик на кнопку Личный кабинет')
    def click_profile_button(self):   
        self.click_element(MainPageLocators.USER_PROFILE_BUTTON)

    @allure.step('Клик на кнопку Конструктор')
    def click_constructor_burder_button(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BURGER_BUTTON)

    @allure.step('Клик на кнопку Лента Заказов')
    def click_feed_orders_button(self):
        self.click_element(MainPageLocators.ORDERS_FEED_BUTTON)

    @allure.step('Ожидание закрытия модального окна')
    def wait_ingredient_modal_disappear(self):
        return self.wait_for_element_hidden(MainPageLocators.HIDDEN_INGREDIENT_MODAL, 10)

    @allure.step('Ожидание загрузки кнопки Оформить заказ')
    def wait_create_order_button_displayed(self):
        self.find_element(MainPageLocators.CREATE_ORDER_BUTTON, 10)

    @allure.step('Клик на кнопку Оформить заказ')
    def click_create_order_button(self):
        self.click_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        return self.get_element(MainPageLocators.ORDER_ID)

    @allure.step('Ожидание загрузки заголовка Ваш заказ начали готовить')
    def wait_cooking_is_start_displayed(self):
        return self.find_element(MainPageLocators.ORDER_COOKING, 10)

    @allure.step('Ожидание загрузки заголовка Детали ингредиента')
    def wait_ingredient_info_title_displayed(self):
        return self.find_element(MainPageLocators.INGREDIENT_INFO_TITLE, 10)
    
    @allure.step('Клик на карточку с ингредиентом')
    def click_ingredient_card(self):
        self.click_element(MainPageLocators.INGREDIENT_CARD)

    @allure.step("Клик на кнопку закрыть в карточке заказа")
    def click_close_order_card(self):
        self.wait_for_element_hidden(MainPageLocators.MODAL_BACKDROP, 6)
        self.click_element(MainPageLocators.CLOSE_ORDER_BUTTON)

    @allure.step('Ожидание загрузки кнопки Закрыть на карточке с ингредиентом')
    def wait_close_ingredient_card_is_active(self):
        self.wait_element_to_be_clickable(MainPageLocators.CLOSE_INGREDIENT_MODAL_BUTTON, 10)

    @allure.step('Клик на кнопку закрыть в картчоке с ингредиентом')
    def click_close_ingredient_card(self):
        self.click_element(MainPageLocators.CLOSE_INGREDIENT_MODAL_BUTTON)
    
    @allure.step('Добавить булочку в конструктор')
    def add_bun_to_constructor(self):
        bun = MainPageLocators.DRAGGABLE_INGREDIENT_CARD
        constructor = MainPageLocators.CONSTRUCTOR_BUN_SLOT
        self.drag_ingredient_to_constructor(bun, constructor)

    @allure.step('Получить значение каунтера')
    def get_value_counter(self):
        return self.get_element(MainPageLocators.AMOUNT_INDICATOR)


    


    

    

