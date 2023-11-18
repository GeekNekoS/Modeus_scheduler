from dotenv import load_dotenv
import os
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from table_processing import when_study

load_dotenv()

option = webdriver.FirefoxOptions()
option.set_preference("dom.webdrive.enabled", False)
option.set_preference("dom.webnotifications.enabled", False)
option.set_preference("media.volume_scale", "0.0")
option.set_preference("general.useragent.override", "yep")

table = when_study()

browser = webdriver.Firefox()
browser.get("https://chat.openai.com/")

xpath="/html/body/div[1]/div[1]/div[2]/div[1]/div/div/button[1]"
browser.find_element(By.XPATH, xpath).click()
time.sleep(5)

login_xpath= '//*[@id="username"]'
lognin_continue_xpath = "/html/body/div/main/section/div/div/div/div[1]/div/form/div[2]/button"
browser.find_element(By.XPATH, login_xpath).send_keys(os.getenv('LOGIN'))
browser.find_element(By.XPATH, lognin_continue_xpath).click()

password_xpath = '//*[@id="password"]'
browser.find_element(By.XPATH, password_xpath).send_keys(os.getenv('PASSWORD'))
time.sleep(2)
password_continue_xpath = '/html/body/div[1]/main/section/div/div/div/form/div[3]/button'
browser.find_element(By.XPATH, password_continue_xpath).click()
time.sleep(6)

letsgo_button_xpath = '/html/body/div[5]/div/div/div/div[2]/div/div[4]/button'
browser.find_element(By.XPATH, letsgo_button_xpath).click()
time.sleep(2)

browser.find_element(By.LINK_TEXT, "Учебные команды").click()


text_xpath = '//*[@id="prompt-textarea"]'
browser.find_element(By.XPATH, text_xpath).send_keys(table + "Какую команду выбрать, если не хочу учиться в субботу?")
time.sleep(2)
send_button_xpath = '/html/body/div[1]/div[1]/div[2]/main/div[1]/div[2]/form/div/div[2]/div/button'
browser.find_element(By.XPATH, send_button_xpath).click()
time.sleep(10)

answer_xpath = '(//*[@class="p-4 gizmo:py-2 justify-center text-base md:gap-6 md:py-6 m-auto"])[last()]'
answer = browser.find_element(By.XPATH, answer_xpath)
print(answer.text.split())




