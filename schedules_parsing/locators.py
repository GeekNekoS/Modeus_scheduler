from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_INPUT = (By.XPATH, "//input[@placeholder='proverka@example.com']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//span[@class='submit']")


class ModeusLocators:
    MODULES = (By.XPATH, "//tbody/tr//span")
    LESSONS = (By.XPATH, "//div[@class='item-name']")
    DIRECTIONS = (By.XPATH, "//div[@class='item-name']")
    DIRECTION_SCHEDULE_BUTTON = (By.XPATH, "//a[@class='no-wrap'][2]")


class TeachersParsingLocators:
    TEACHERS_CARDS = (By.XPATH, "//div[@class='text']")
    PAGES_HREFS = (By.XPATH, "//div[@class='alpha-navigation']/a")


class LogoutLocators:
    # LOG_OUT = (By.XPATH, "//img[@class='user-pic__image']")
    # LOG_OUT_BUTTON = (By.XPATH, "//*[text()='Выйти']")
    pass
