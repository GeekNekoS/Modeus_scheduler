from parsing.locators import *
from parsing.base_page import BaseClass
from selenium.common.exceptions import TimeoutException as TE
from selenium import webdriver


class LoginPage(BaseClass):
    # Log in
    def enter_login(self, login: str) -> webdriver:
        return self.find_element(LoginLocators.LOGIN_INPUT, time=self.time).send_keys(login)

    def enter_password(self, password: str) -> webdriver:
        return self.find_element(LoginLocators.PASSWORD_INPUT, time=self.time).send_keys(password)

    def click_on_the_login_button(self) -> webdriver:
        return self.find_element(LoginLocators.LOGIN_BUTTON, time=self.time).click()

    def check_logedin(self) -> bool:
        try:
            self.find_element(LoginLocators.H4_CHOOSING_MODULES, time=self.time)
            return True
        except:
            return False

    # Log out


class ModeusPage(BaseClass):
    def get_modules(self) -> webdriver:
        return self.find_elements(ModeusLocators.MODULES, time=self.time)

    def get_disciplines(self) -> webdriver:
        return self.find_elements(ModeusLocators.DISCIPLINES_DIRECTIONS, time=self.time)

    def get_directions(self) -> webdriver:
        return self.find_elements(ModeusLocators.DISCIPLINES_DIRECTIONS, time=self.time)

    def find_element_by_xpath(self, xpath: str) -> webdriver:
        return self.find_element((By.XPATH, xpath), time=self.time)

    def find_elements_by_xpath(self, xpath: str) -> webdriver:
        return self.find_elements((By.XPATH, xpath), time=self.time)

    def go_to_disciplines_page(self, disciplines_page_url: str) -> webdriver:
        return self.get_connect(disciplines_page_url)

    def get_schedule_url(self) -> webdriver:
        return self.find_element(ModeusLocators.SCHEDULE_URL, time=self.time)  # .get_attribute("href")

    def go_to(self, url: str) -> webdriver:
        return self.get_connect(url)

    def get_popover(self) -> webdriver:
        return self.find_element(ModeusLocators.POPOVER, time=self.time)

    def get_teachers_name(self) -> webdriver:
        return self.find_element(ModeusLocators.TEACHERS_NAME, time=self.time).text.replace("\n", ", ")

    def get_h3_point(self) -> webdriver:
        return self.find_element(ModeusLocators.H3_MY_SCHEDULE, time=self.time)


class TeachersParsing(BaseClass):
    def get_pages(self) -> list[str]:
        pages = self.find_elements(TeachersParsingLocators.PAGES_HREFS, time=self.time)
        urls = []
        for page in pages:
            urls.append(page.get_attribute("href"))
        return urls

    def go_to_teachers_page(self):
        url = 'https://urfu.ru/ru/about/personal-pages'
        return self.get_connect(url)

    def get_teachers_cards(self) -> list:
        try:
            return self.find_elements(TeachersParsingLocators.TEACHERS_CARDS, time=self.time)
        except TE:
            return []
