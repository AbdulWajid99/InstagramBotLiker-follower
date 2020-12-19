import selenium
from selenium import webdriver
import time


class InstaBot_follower:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(
            executable_path="Your path")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)
        driver.find_element_by_name("username").send_keys(self.username)
        password = driver.find_element_by_name("password")
        password.send_keys(self.password)
        password.submit()
        time.sleep(3)

    def findUser(self, userName):
        driver = self.driver
        driver.get("https://www.instagram.com/"+userName)
        time.sleep(2)

    def followBot(self):
        driver = self.driver
        driver.find_element_by_xpath('//button[text()="Follow Back"]').click()


instabotfollower = InstaBot_follower("your id", "pass")
instabotfollower.login()
instabotfollower.findUser("User to follow")
instabotfollower.followBot()
