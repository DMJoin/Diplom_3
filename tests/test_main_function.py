import allure
from pages.main_page import *
from pages.order_feed_page import *
from pages.login_page import *
from urls import main_page_url, orders_feed_url



class TestMainFunction:

    @allure.title('Успешный переход по клику на кнопку «Конструктор»')
    def test_click_button_constructor_succes(self, driver):
        main_page = MainPage(driver)
    
        main_page.wait_for_login_button_displayed()
        main_page.wait_window_is_hidden()
        main_page.click_constructor_burder_button()
        main_page.wait_for_login_button_displayed()
        current_url = main_page.get_current_url()

        assert current_url == main_page_url

    @allure.title('Успешный переход по клику на кнопку «Лента заказов»')
    def test_click_button_order_feed_success(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.wait_for_login_button_displayed()
        main_page.wait_window_is_hidden()
        main_page.click_feed_orders_button()
        order_feed_page.wait_for_orders_feed_visible()
        current_url = main_page.get_current_url()

        assert current_url == orders_feed_url

    @allure.step('При клике на ингредиент появляется всплывающее окно с деталями')
    def test_click_ingredient_show_modal_with_ingredients(self, driver):
        main_page = MainPage(driver)

        main_page.wait_for_login_button_displayed()
        main_page.wait_window_is_hidden()
        main_page.click_ingredient_card()

        assert main_page.wait_ingredient_info_title_displayed()

    @allure.title('Всплывающее окно с деталями ингредиентов закрывается кликом по крестику')
    def test_click_close_button_closed_modal(self, driver):
        main_page = MainPage(driver)

        main_page.wait_for_login_button_displayed()
        main_page.wait_window_is_hidden()
        main_page.click_ingredient_card()
        main_page.wait_ingredient_info_title_displayed()
        main_page.wait_close_ingredient_card_is_active()
        main_page.click_close_ingredient_card()

        assert main_page.wait_ingredient_modal_disappear()

    @allure.title('После добавления ингредиента в заказ увеличивается каунтер данного ингредиента')
    def test_add_igredient_counter_increases(self, driver):
        main_page = MainPage(driver)

        main_page.wait_for_login_button_displayed()
        main_page.wait_window_is_hidden()
        value_counter_first = main_page.get_value_counter()
        main_page.add_bun_to_constructor()
        value_counter_second = main_page.get_value_counter()
        main_page.wait_window_is_hidden()
        
        assert value_counter_first < value_counter_second

    @allure.title('Авторизованный пользователь умпешно оформляет заказ')
    def test_auth_user_create_order_succes(self, driver, create_user, delete_user):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        response = create_user["response"]
        response_text = response.json()
        main_page.wait_for_login_button_displayed()
        main_page.wait_window_is_hidden()
        main_page.click_profile_button()
        login_page.wait_login_page_for_load()
        login_page.enter_email(create_user['email'])
        login_page.enter_password(create_user['password'])
        login_page.click_login_button()
        main_page.wait_create_order_button_displayed()
        main_page.add_bun_to_constructor()
        main_page.click_create_order_button()

        assert main_page.wait_cooking_is_start_displayed()

        access_token = response_text["accessToken"]
        delete_user(access_token)















