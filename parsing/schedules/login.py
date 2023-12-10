from selenium.webdriver.chrome.options import Options
from parsing.page_object import LoginPage
from selenium import webdriver
import os

from dotenv import load_dotenv
load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')


def is_user_logedin_modeus(user_login, user_password):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome()  # options=chrome_options
    driver.maximize_window()

    # login
    login_page = LoginPage(driver)
    login_page.go_to_modules_page()
    login_page.enter_login(user_login)
    login_page.enter_password(user_password)
    login_page.click_on_the_login_button()

    loged_in = login_page.check_logedin()
    if loged_in:
        return True
    else:
        return False
