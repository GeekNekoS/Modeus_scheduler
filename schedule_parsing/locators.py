from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_INPUT = (By.XPATH, "//input[@placeholder='proverka@example.com']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//span[@class='submit']")


class ModeusLocators:
    MATH_BUTTON = (By.XPATH, "//div[text()=' Математика ']")
    MATH_BASIC_LEVEL_BUTTON = (By.XPATH, "//div[text()=' Математика. Базовый уровень. ']")
    MODULE_SCHEDULE_BUTTON = (By.XPATH, "//a[text()=' Расписание модуля ']")


class LogoutLocators:
    # LOG_OUT = (By.XPATH, "//img[@class='user-pic__image']")
    # LOG_OUT_BUTTON = (By.XPATH, "//*[text()='Выйти']")
    pass
