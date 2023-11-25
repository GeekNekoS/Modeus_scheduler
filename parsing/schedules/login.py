import os


def login(page):
    page.go_to_modules_page()
    page.enter_login(os.getenv('LOGIN'))
    page.enter_password(os.getenv('PASSWORD'))
    page.click_on_the_login_button()

    return page
