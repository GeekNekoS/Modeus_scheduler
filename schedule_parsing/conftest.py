from schedule_parsing.page_object import LoginPage
from selenium import webdriver
import logging
import pytest
import time
import os

from dotenv import load_dotenv

load_dotenv()
LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def driver():
    # options = Options()
    # options.page_load_strategy = 'eager'
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()

    LOGGER.info('The browser opens on the main page')
    modeus_main_page = LoginPage(driver)

    LOGGER.info('The auth page opens')
    modeus_main_page.go_to_auth_page()

    LOGGER.info('Login entered')
    modeus_main_page.enter_login(os.getenv('LOGIN'))

    LOGGER.info('Password entered')
    modeus_main_page.enter_password(os.getenv('PASSWORD'))

    LOGGER.info('The login button is pressed')
    modeus_main_page.click_on_the_login_button()

    LOGGER.info('Authorization upload')
    time.sleep(3)

    LOGGER.info('Running autotests')
    yield driver

    # LOGGER.info('Logging out of my account')
    # modeus_main_page.log_out()

    # LOGGER.info('Closing the browser')
    # driver.quit()

# выписать действие регистрации в функции driver в отдельную фикстуру
