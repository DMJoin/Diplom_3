import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import *


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание загрузки Ленты заказов')
    def wait_for_orders_feed_visible(self):
        self.find_element(OrderFeedPageLocators.ORDER_FEED_TITLE, 20)

    @allure.step('Ожидание загрузки заголовка Состав')
    def wait_for_order_details_visible(self):
        return self.find_element(OrderFeedPageLocators.ORDER_INGREDIENTS_LIST, 10)
    
    allure.step('Получить номер первого заказа')
    def get_first_order_number(self):
        return self.get_element(OrderFeedPageLocators.FIRST_ORDER_NUMBER)
    
    @allure.step('Скролл до заказа')
    def scroll_to_order(self, text: str):
        locator = (By.XPATH, f"//*[text()='{text}']")
        self.scroll_to_element(locator)
        return self.find_element(locator)

    @allure.step('Клик по первому заказу в ленте заказаов')
    def click_first_order_in_list(self):
        self.click_element(OrderFeedPageLocators.ORDER_IN_LIST)

    @allure.step('Получить количество заказов за сегодня')
    def get_todays_orders_count(self):
        return self.get_element(OrderFeedPageLocators.TODAY_ORDERS_COUNT)
    
    @allure.step('Получить общее количество заказов')
    def get_total_orders_count(self):
        return self.get_element(OrderFeedPageLocators.TOTAL_ORDERS_COUNT)
    
    @allure.step('Получить номер заказа в статусе В работе')
    def get_current_order_in_progress_id(self, timeout=10):
        self.find_element(OrderFeedPageLocators.CURRENT_ORDERS_IN_PROGRESS)
        return self.get_element(OrderFeedPageLocators.CURRENT_ORDERS_IN_PROGRESS)
    
    @allure.step('Ожидание загрузки заголовка Лента заказов')
    def wait_order_feed_header_displayed(self):
        self.find_element(OrderFeedPageLocators.ORDER_FEED_TITLE, 10)


    