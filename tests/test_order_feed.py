import allure
from pages.login_page import *
from pages.main_page import *
from pages.order_feed_page import *
from pages.profile_page import *


class TestOrderFeed:

    @allure.title('Eсли кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_open_modal_with_details(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)      

        main_page.wait_for_login_button_displayed()
        main_page.wait_window_is_hidden()
        main_page.click_feed_orders_button()
        order_feed_page.wait_for_orders_feed_visible()
        order_feed_page.click_first_order_in_list()

        assert order_feed_page.wait_for_order_details_visible()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_orders_user_displayed_order_feed(self, driver, create_user, delete_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)    

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
        main_page.wait_cooking_is_start_displayed()
        main_page.click_close_order_card()
        main_page.wait_window_is_hidden()
        main_page.click_profile_button()
        profile_page.wait_profile_page_load
        main_page.wait_window_is_hidden()
        profile_page.click_history_order_button()
        order = order_feed_page.get_first_order_number()  
        main_page.click_feed_orders_button()
        order_feed_page.wait_order_feed_header_displayed()

        assert order_feed_page.scroll_to_order(text=order)
        
        access_token = response_text["accessToken"]
        delete_user(access_token)
        
    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_create_new_order_counter_increases(self, driver, create_user, delete_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
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
        main_page.click_feed_orders_button()
        order_feed_page.wait_for_orders_feed_visible()
        orders_before = order_feed_page.get_total_orders_count()
        main_page.click_constructor_burder_button()
        main_page.add_bun_to_constructor()
        main_page.click_create_order_button()
        main_page.wait_cooking_is_start_displayed()
        main_page.click_close_order_card()
        main_page.wait_window_is_hidden()
        main_page.click_feed_orders_button()
        order_feed_page.wait_for_orders_feed_visible()
        orders_after = order_feed_page.get_total_orders_count()

        assert orders_after > orders_before

        access_token = response_text["accessToken"]
        delete_user(access_token)

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_create_new_order_counter_today_increases(self, driver, create_user, delete_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
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
        main_page.click_feed_orders_button()
        order_feed_page.wait_for_orders_feed_visible()
        orders_before = order_feed_page.get_todays_orders_count()
        main_page.click_constructor_burder_button()
        main_page.add_bun_to_constructor()
        main_page.click_create_order_button()
        main_page.wait_cooking_is_start_displayed()
        main_page.click_close_order_card()
        main_page.wait_window_is_hidden()
        main_page.click_feed_orders_button()
        order_feed_page.wait_for_orders_feed_visible()
        orders_after = order_feed_page.get_todays_orders_count()

        assert orders_after > orders_before

        access_token = response_text["accessToken"]
        delete_user(access_token)


    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_number_order_append_in_work_status(self, driver, create_user, delete_user):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
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
        main_page.wait_cooking_is_start_displayed()
        order_number = "0" + main_page.get_order_number()
        main_page.click_close_order_card()
        main_page.wait_window_is_hidden()
        main_page.click_feed_orders_button()
        order_feed_page.wait_for_orders_feed_visible()
        order_number_in_status = order_feed_page.get_current_order_in_progress_id()
        
        assert order_number > order_number_in_status

        access_token = response_text["accessToken"]
        delete_user(access_token)








