#import dependies
import selenium
from selenium import webdriver
import time


class InstaBot_like:
    # constructer for variable
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(
            executable_path="Chrome_Driver_path")

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
    #   password.submit()
        time.sleep(3)

# search for id
    def findUser(self, userForlike):
        driver = self.driver
        driver.get("https://www.instagram.com/"+userForlike)

# like the posts
    def likePosts(self, num):
        driver = self.driver
        driver.find_element_by_class_name("v1Nh3").click()

        i = 1
        while i <= num:
            time.sleep(1)

            driver.find_element_by_class_name(
                "fr66n").click()  # like a posts  #_8-yf5

            driver.find_element_by_class_name(
                "coreSpriteRightPaginationArrow").click()  # Go to next post
            time.sleep(1)
            i = i+1

        driver.get("https://www.instagram.com/")  # Back to Insta main page
        time.sleep(2)


# first function give your insta id uname and pass
instaBot = InstaBot_like("yourid", "pass")

# second function login with given credentials
instaBot.login()

# third function search your id
instaBot.findUser("User To Follow")
# fourth one selects a picture to like
num = 19  # number of pics to like
instaBot.likePhotos(num)
