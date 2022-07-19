from services import ChromeService, ExcelService
import os
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

# get info from .env
username = os.getenv('USER_NAME')
password = os.getenv('PASS_WORD')
website = os.getenv('WEBSITE')

excel_service = ExcelService()
chrome_service = ChromeService()

message = "Happy Birthday. Wish you are the best!"

file_name = "data.xlsx"


def get_all_user_have_birthday_today():
    user_name = list(excel_service.get_column_data(file_name, "Name"))
    instagrams = list(excel_service.get_column_data(file_name, "Insta"))
    birthday_month, birthday_day = excel_service.get_date_of_birth_of_all_user(
        file_name)
    dictionary = {}
    for index in range(len(user_name)):
        # dictionary["a"] = [1,2,3]
        dictionary[user_name[index]] = [
            birthday_month[index], birthday_day[index], instagrams[index]]
    all_user_have_birthday_today = []
    today = [datetime.now().month, datetime.now().day]
    print(today)
    for i in dictionary:
        print(dictionary[i][0:2])
        if today == dictionary[i][0:2]:
            # append instagram of user have birthday today
            all_user_have_birthday_today.append(dictionary[i][-1])
    return all_user_have_birthday_today


def __main__():
    chrome = chrome_service.open_browser()
    chrome_service.access_url(website + username + "/", chrome)
    chrome_service.login(username, password, chrome)
    users = get_all_user_have_birthday_today()
    for user in users:
        chrome_service.access_url(website + user + "/", chrome)
        chrome_service.send_message(message, chrome)
    chrome.close()


__main__()
