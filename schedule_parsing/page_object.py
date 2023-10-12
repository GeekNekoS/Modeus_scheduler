from schedule_parsing.locators import *
from schedule_parsing.base_page import BaseClass
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys


class LoginPage(BaseClass):
    # Log in
    def enter_login(self, login):
        return self.find_element(LoginLocators.LOGIN_INPUT, time=self.time).send_keys(login)

    def enter_password(self, password):
        return self.find_element(LoginLocators.PASSWORD_INPUT, time=self.time).send_keys(password)

    def click_on_the_login_button(self):
        return self.find_element(LoginLocators.LOGIN_BUTTON, time=self.time).click()

    # Log out


class ModeusPage(BaseClass):
    def click_math_button(self):
        return self.find_element(ModeusLocators.MATH_BUTTON, time=self.time).click()

    def click_math_basic_level_button(self):
        return self.find_element(ModeusLocators.MATH_BASIC_LEVEL_BUTTON, time=self.time).click()

    def click_on_module_math_basic_level_button(self):
        return self.find_element(ModeusLocators.MODULE_SCHEDULE_BUTTON, time=self.time).click()

    def click_on_english_module(self):
        return self.find_elements(ModeusLocators.MODULES_BUTTONS, time=self.time)[0].click()

    def click_on_all_module(self):
        return self.find_elements(ModeusLocators.MODULES_BUTTONS, time=self.time)[1].click()

    def click_on_english_lesson(self):
        self.find_element(ModeusLocators.ENGLISH_LESSON, time=self.time).click()

    def click_on_english_level_b2_c1(self):
        self.find_element(ModeusLocators.ENGLISH_LEVEL_BUTTON, time=self.time).click()

    def click_on_english_schedule_button(self):
        self.find_element(ModeusLocators.ENGLISH_SCHEDULE_BUTTON, time=self.time).click()

    def click_on_itis_lesson(self):
        self.find_element(ModeusLocators.ITIS_LESSON_BUTTON, time=self.time).click()

    def click_on_itis_1(self):
        self.find_element(ModeusLocators.ITIS_1_MODULE, time=self.time).click()

    def click_on_itis_1_schedule(self):
        self.find_element(ModeusLocators.ITIS_1_SCHEDULE, time=self.time).click()
