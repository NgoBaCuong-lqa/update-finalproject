from selenium import webdriver
from parameterized import parameterized
import unittest
import sys
import time
from Page_Object.Create_Account import Account

sys.path.append("C:\My-Final-Project-main\FInalProjects")


class CreateAccountt(unittest.TestCase):
    baseURL = "http://automationpractice.com/index.php"

    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    def test_createanaccount(self, browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome(executable_path=r"C:\Driver\chromedriver.exe")
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"C:\Driver\geckodriver.exe")
            time.sleep(3)
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
