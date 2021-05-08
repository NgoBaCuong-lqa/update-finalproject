from selenium import webdriver
import unittest
from Page_Object.share_to_tweet import share_to_tweets
import sys
import time
sys.path.append("C:\My-Final-Project-main\FInalProjects")

class share_to_tweet(unittest.TestCase):

    baseURL = "http://automationpractice.com/index.php"
    driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")

    def setUp(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_sharetotweet(self):
        lp = share_to_tweets(self.driver)
        lp.click_img2()
        lp.click_tweet()

if __name__ == '__main__':
    unittest.main()