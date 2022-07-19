from calendar import c
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
# sec everytime sleep
sec = 4

# check if this is the first time of login
first_time = True


class ExcelService:
    @classmethod
    def get_all_data(cls, file_name):
        return pd.read_excel(file_name)

    @classmethod
    def get_column_data(cls, file_name, column_name):
        return ExcelService.get_all_data(file_name)[column_name]


class ChromeService:
    @classmethod
    def login(cls, p_username, p_password, chrome):
        login_btn = chrome.find_element(By.CLASS_NAME, "_acap")
        login_btn.click()
        time.sleep(sec)

        username = chrome.find_element(By.NAME, "username")
        username.send_keys(p_username)
        password = chrome.find_element(By.NAME, "password")
        password.send_keys(p_password)
        time.sleep(sec)

        password.send_keys(Keys.RETURN)
        time.sleep(sec)

        save_info = chrome.find_element(By.CLASS_NAME, "L3NKy")
        save_info.click()

        time.sleep(sec)

    @classmethod
    def send_message(cls, p_message, chrome):
        message = chrome.find_element(By.CLASS_NAME, "_acap")
        message.click()
        time.sleep(sec)

        global first_time
        if first_time:
            chrome.find_element(By.CLASS_NAME, "_a9_1").click()
            time.sleep(sec)
            first_time = False

        message_area = chrome.find_element(By.TAG_NAME, "textarea")
        message_area.send_keys(p_message)
        message_area.send_keys(Keys.RETURN)
        time.sleep(sec)

    @classmethod
    def open_browser(cls):
        chrome = webdriver.Chrome()
        time.sleep(sec)
        return chrome

    @classmethod
    def access_url(cls, url, chrome):
        chrome.get(url)
        time.sleep(sec)
