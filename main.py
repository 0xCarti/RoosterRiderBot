import getopt
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeType

######## GLOBAL VARIABLES ########
USERNAME = ''
PASS = ''
######## GLOBAL VARIABLES ########


def readArgs():
    global USERNAME, PASS
    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:p:", ["uname=", "pword="])
    except getopt.GetoptError:
        print('GetOpt Error')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Command Line Args:\r\n\t-u <username\r\n\t-p <password>')
            sys.exit()
        elif opt in ("-u", "--uname"):
            USERNAME = arg
            print("Username = {}".format(USERNAME))
        elif opt in ("-p", "--pword"):
            PASS = arg
            print('Password = {}'.format(PASS))

    if len(USERNAME) == 0 or len(PASS) == 0:
        USERNAME = input('Please enter your username: ')
        PASS = input('Please enter your password: ')


def login(username: str, password: str):
    email_box = WebDriverWait(browser, 60).until((EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/form/div/div[1]/input'))))
    email_box.clear()
    email_box.send_keys(USERNAME)

    pass_box = WebDriverWait(browser, 60).until((EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/form/div/div[2]/input'))))
    pass_box.clear()
    pass_box.send_keys(PASS)

    login_button = WebDriverWait(browser, 60).until((EC.presence_of_element_located((By.XPATH, '/html/body/div/div[3]/form/button'))))
    login_button.click()

    while True:
        pass

def scroll_next_week():
    pass


# Setup browser
browser = webdriver.Chrome(executable_path=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
browser.maximize_window()
browser.implicitly_wait(10)

# Navigate to login page
browser.get("https://fi.usehurrier.com/app/rooster/web/login")
readArgs()
login(USERNAME, PASS)

# Teardown browser and close
browser.close()
browser.quit()
