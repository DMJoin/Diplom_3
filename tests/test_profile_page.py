import allure
from pages.main_page import *
from pages.profile_page import *
from pages.login_page import *


class TestProfilePage:

    @allure.title('Переход по клику в «Личный кабинет»')
    def test_redirect_to_profile_page(self, driver, create_user, delete_user):
        main_page = MainPage(driver)
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
        main_page.click_profile_button()
        profile_page.wait_profile_page_load()    
        current_url = profile_page.get_current_url()

        assert "/account/profile" in current_url

        access_token = response_text["accessToken"]
        delete_user(access_token)

    @allure.title('Переход в раздел «История заказов»')
    def test_redirect_to_history_page(self, driver, create_user, delete_user):
        main_page = MainPage(driver)
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
        main_page.click_profile_button()
        profile_page.wait_profile_page_load()
        main_page.wait_window_is_hidden()
        profile_page.click_history_order_button()
        profile_page.wait_profile_page_load()
        current_url = profile_page.get_current_url()

        assert "/account/order-history" in current_url

        access_token = response_text["accessToken"]
        delete_user(access_token)

    @allure.title('Выход из аккаунта')
    def test_logout_from_profile_page(self, driver, create_user, delete_user):
        main_page = MainPage(driver)
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
        main_page.click_profile_button()
        profile_page.wait_profile_page_load()
        main_page.wait_window_is_hidden()
        profile_page.click_logout_button()
        login_page.wait_login_page_for_load()
        current_url = login_page.get_current_url()
        
        assert "/login" in current_url

        access_token = response_text["accessToken"]
        delete_user(access_token)




        


        


