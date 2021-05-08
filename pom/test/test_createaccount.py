from selenium import webdriver
import unittest
from Page_Object.Create_Account import Account
import sys
import time

sys.path.append(r'C:\Users\Admin\PycharmProjects\UpdateFinalproject')


class createaccount(unittest.TestCase):
    baseURL = "http://automationpractice.com/index.php"



    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

    def test_createanaccount(self):
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        email = "abc123"
        lp = Account(self.driver)
        lp.click_signin()
        lp.set_emailaddress(email)
        lp.click_createanaccount()
        time.sleep(5)

    def tearDown(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()
