from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# sec everytime sleep
sec = 4

# check if this is the first time of login
first_time = True

# get info from .env
username = os.getenv('USER_NAME')
password = os.getenv('PASS_WORD')
website = os.getenv('WEBSITE')


def open_browser():
    global chrome
    chrome = webdriver.Chrome()
    time.sleep(sec)


def access_url(url):
    chrome.get(url)
    time.sleep(sec)


def login(p_username, p_password):
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


def send_message(p_message):
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


def get_all_insta_names():
    data = pd.read_excel("data.xlsx")
    return data["Insta"]


def __main__():
    message = "Have a good day!"
    open_browser()
    access_url(website + username + "/")
    login(username, password)

    for name in get_all_insta_names():
        access_url(website + name + "/")
        send_message(message)

    chrome.close()


__main__()
