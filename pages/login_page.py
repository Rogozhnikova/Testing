from .base_page import BasePage
from .locators import LoginPageLocators
from time import sleep


class LoginPage(BasePage):
    # func for registration new user for test cases with login user
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

    # func for check that there is login form on page
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    # func for check that login form appear after redirect on login page
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    #check that text login present in URL
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Word "login" is not presented in URL'

    # func for check that there is registration form on page
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"