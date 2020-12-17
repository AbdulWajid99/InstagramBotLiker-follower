import selenium
from selenium import webdriver
import time


class InstaBot:
    # constructore for variable
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(
            executable_path="E:\Data_Scientist\Python\Projects\Intagram like bot\chromedriver_win32\chromedriver.exe")

# to login from given username and password
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")  # open insta main page
        time.sleep(3)
        driver.find_element_by_name("username").send_keys(
            self.username)  # fill usermae with given username
        password = driver.find_element_by_name("password")
        password.send_keys(self.password)  # fill password with given password
        password.submit()  # submit it
        time.sleep(3)

        password.submit()
        time.sleep()


# first function give your insta id uname and pass
instaBot = InstaBot("deadtillnow__", "ronaldocr7")
# second function login with given credentials
instaBot.login()
