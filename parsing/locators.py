from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_INPUT = (By.XPATH, "//input[@placeholder='proverka@example.com']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//span[@class='submit']")
    H4_CHOOSING_MODULES = (By.XPATH, "//h4[text()='Выбор модулей']")


class ModeusLocators:
    MODULES = (By.XPATH, "//tbody/tr//span")
    DISCIPLINES_DIRECTIONS = (By.XPATH, "//div[@class='item-name']")
    SCHEDULE_URL = (By.XPATH, "//a[text()=' Расписание модуля ']")
    POPOVER = (By.XPATH, "//ngb-popover-window")
    TEACHERS_NAME = (By.XPATH, "//div[@class='ng-star-inserted']")
    H3_MY_SCHEDULE = (By.XPATH, "//h3[text()='Мое расписание']")


class TeachersParsingLocators:
    TEACHERS_CARDS = (By.XPATH, "//div[@class='text']")
    PAGES_HREFS = (By.XPATH, "//div[@class='alpha-navigation']/a")


class LogoutLocators:
    # LOG_OUT = (By.XPATH, "//img[@class='user-pic__image']")
    # LOG_OUT_BUTTON = (By.XPATH, "//*[text()='Выйти']")
    pass
