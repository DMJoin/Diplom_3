import allure
from pages.main_page import *
from pages.login_page import *
from pages.recovery_password_page import *


class TestRecoveryPassword:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_click_recovery_password_move_password_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_password_page = RecoveryPasswordPage(driver)

        main_page.wait_for_login_button_displayed()
        main_page.wait_window_is_hidden()
        main_page.click_profile_button()
        login_page.wait_login_page_for_load()
        login_page.click_password_recovery_button()
        recovery_password_page.wait_recovery_password_header_visible()
        current_url = login_page.get_current_url()

        assert "forgot-password" in current_url

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_recovery_password_with_correct_email(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_password_page = RecoveryPasswordPage(driver)

        main_page.wait_for_login_button_displayed()
        main_page.wait_window_is_hidden()
        main_page.click_profile_button()
        login_page.wait_login_page_for_load()
        login_page.click_password_recovery_button()
        login_page.enter_email("test@gmail.com")
        recovery_password_page.click_to_recovery_button()
        recovery_password_page.wait_code_input_visible()
        current_url = login_page.get_current_url()

        assert "/reset-password" in current_url

    @allure.title('Клик по кнопке показать/скрыть пароль подсвечивает поле')
    def test_click_button_password_field_is_active(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        recovery_password_page = RecoveryPasswordPage(driver)

        main_page.wait_for_login_button_displayed()
        main_page.wait_window_is_hidden()
        main_page.click_profile_button()
        login_page.wait_login_page_for_load()
        login_page.click_password_recovery_button()
        login_page.enter_email("test@gmail.com")
        recovery_password_page.click_to_recovery_button()
        main_page.wait_window_is_hidden()
        recovery_password_page.click_to_show_password_button()
        
        assert recovery_password_page.password_field_is_active()

        





