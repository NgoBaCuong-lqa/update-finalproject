from selenium import webdriver
import unittest
from Page_Object.send_to_friend import Send_to_friends
import sys
import time

sys.path.append("C:\My-Final-Project-main\FInalProjects")


class sendtofriend(unittest.TestCase):
    baseURL = "http://automationpractice.com/index.php"

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

    def test_newsletter(self):
        emailaddress = "cuongnb.lqa@gmail.com"
        friend_name = "cuong"
        lp = Send_to_friends(self.driver)
        lp.click_img()
        lp.click_button_send_to_friend()
        lp.setfriendname(emailaddress)
        lp.setemailaddress(friend_name)
        lp.click_send()
        time.sleep(5)

    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
