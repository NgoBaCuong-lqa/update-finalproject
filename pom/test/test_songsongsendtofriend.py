from selenium import webdriver
import unittest
import sys
import time
from Page_Object.send_to_friend import Send_to_friends
from parameterized import parameterized

sys.path.append("C:\My-Final-Project-main\FInalProjects")


class sendtofriend(unittest.TestCase):
    baseURL = "http://automationpractice.com/index.php"

    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    def test_newsletter(self, browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome(executable_path=r"C:\Driver\chromedriver.exe")
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"C:\Driver\geckodriver.exe")
            time.sleep(3)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
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
