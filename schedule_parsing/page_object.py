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
    # def click_math_button(self):
    #     return self.find_element(ModeusLocators.MATH_BUTTON, time=self.time).click()

    # def click_math_basic_level_button(self):
    #     return self.find_element(ModeusLocators.MATH_BASIC_LEVEL_BUTTON, time=self.time).click()

    def click_on_lesson_module_button(self):
        return self.find_element(ModeusLocators.MODULE_SCHEDULE_BUTTON, time=self.time).click()

    def click_on_english_module(self):
        return self.find_elements(ModeusLocators.MODULES_BUTTONS, time=self.time)[0].click()

    def click_on_all_module(self):
        return self.find_elements(ModeusLocators.MODULES_BUTTONS, time=self.time)[1].click()

    def click_on_english_lesson(self):
        return self.find_element(ModeusLocators.ENGLISH_LESSON, time=self.time).click()

    def click_on_english_level_b2_c1(self):
        return self.find_element(ModeusLocators.ENGLISH_LEVEL_BUTTON, time=self.time).click()

    def click_on_itis_lesson(self):
        return self.find_element(ModeusLocators.ITIS_LESSON_BUTTON, time=self.time).click()

    def click_on_itis_1(self):
        return self.find_element(ModeusLocators.ITIS_1_MODULE, time=self.time).click()

    def click_on_itis_2(self):
        return self.find_element(ModeusLocators.ITIS_2_MODULE, time=self.time).click()

    def click_on_itis_3(self):
        return self.find_element(ModeusLocators.ITIS_3_MODULE, time=self.time).click()

    def click_on_itis_4(self):
        return self.find_element(ModeusLocators.ITIS_4_MODULE, time=self.time).click()

    def click_on_itis_5(self):
        return self.find_element(ModeusLocators.ITIS_5_MODULE, time=self.time).click()

    def click_on_itis_6(self):
        return self.find_element(ModeusLocators.ITIS_6_MODULE, time=self.time).click()

    def click_on_itis_7(self):
        return self.find_element(ModeusLocators.ITIS_7_MODULE, time=self.time).click()

    def click_on_itis_8(self):
        return self.find_element(ModeusLocators.ITIS_8_MODULE, time=self.time).click()

    def click_on_itis_9(self):
        return self.find_element(ModeusLocators.ITIS_9_MODULE, time=self.time).click()

    def click_on_itis_10(self):
        return self.find_element(ModeusLocators.ITIS_10_MODULE, time=self.time).click()

    def click_on_itis_11(self):
        return self.find_element(ModeusLocators.ITIS_11_MODULE, time=self.time).click()

    def click_on_itis_12(self):
        return self.find_element(ModeusLocators.ITIS_12_MODULE, time=self.time).click()

    def click_on_itis_13(self):
        return self.find_element(ModeusLocators.ITIS_13_MODULE, time=self.time).click()

    def click_on_history_lesson(self):
        return self.find_element(ModeusLocators.HISTORY, time=self.time).click()

    def click_on_russian_history(self):
        return self.find_element(ModeusLocators.RUSSIAN_HISTORY, time=self.time).click()

    def click_on_history_of_russian_civilization(self):
        return self.find_element(ModeusLocators.HISTORY_OF_RUSSIAN_CIVILIZATION, time=self.time).click()

    def click_on_math_lesson(self):
        return self.find_element(ModeusLocators.MATH, time=self.time).click()

    def click_on_math_basic_level(self):
        return self.find_element(ModeusLocators.MATH_BASIC_LEVEL, time=self.time).click()

    def click_on_math_pro_level(self):
        return self.find_element(ModeusLocators.MATH_PRO_LEVEL, time=self.time).click()
