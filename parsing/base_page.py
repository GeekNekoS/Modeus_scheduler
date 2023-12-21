from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class BaseClass:
    def __init__(self, driver):
        self.driver = driver
        self.time = 10
        self.modules_url = "https://urfu.modeus.org/learning-path-selection/menus"

    def find_element(self, locator: tuple, time=10) -> webdriver:
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator: tuple, time=10) -> webdriver:
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def get_elem_by_custom_xpath(self, xpath: str) -> webdriver:
        return self.find_element((By.XPATH, xpath), time=1)

    def get_elems_by_custom_xpath(self, xpath: str) -> webdriver:
        return self.find_elements((By.XPATH, xpath), time=1)

    def go_to_modules_page(self) -> webdriver:
        return self.driver.get(self.modules_url)

    def get_connect(self, url: str, retry=3) -> webdriver:
        """Prevents from possible connection breaks"""
        try:
            self.driver.get(url=url)
        except Exception as exception:
            if retry:
                print(f"\033[38;5;{196}mReconnecting\033[0;0m")
                print(exception)
                return self.get_connect(url, retry=(retry - 1))
            else:
                raise
        else:
            return self.driver.get(url=url)
