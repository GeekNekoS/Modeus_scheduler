from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:
    def __init__(self, driver):
        self.driver = driver
        self.time = 10
        self.auth_url = "https://urfu.modeus.org/"
        self.lessons_url = "https://urfu.modeus.org/learning-path-selection/menus/45f2857b-6745-4d7a-8677-002f0b3e02e0"
        self.modules_url = "https://urfu.modeus.org/learning-path-selection/menus"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_auth_page(self):
        return self.driver.get(self.auth_url)

    def go_to_lessons_page(self):
        return self.driver.get(self.lessons_url)

    def go_to_modules_page(self):
        return self.driver.get(self.modules_url)
