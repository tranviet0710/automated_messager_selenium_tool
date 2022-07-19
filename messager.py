import os
from dotenv import load_dotenv
from services import ExcelService, ChromeService
load_dotenv()

# get info from .env
username = os.getenv('USER_NAME')
password = os.getenv('PASS_WORD')
website = os.getenv('WEBSITE')


message = "Wish you all the best!"

def __main__():
    chrome_service = ChromeService()
    chrome = chrome_service.open_browser()
    chrome_service.access_url(website + username + "/", chrome)
    chrome_service.login(username, password, chrome)
    get_all_insta_names = ExcelService.get_column_data("data.xlsx", "Insta")
    for name in get_all_insta_names:
        chrome_service.access_url(website + name + "/", chrome)
        chrome_service.send_message(message, chrome)

    chrome.close()

__main__()
