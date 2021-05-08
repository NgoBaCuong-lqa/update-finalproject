from selenium import webdriver
import unittest
from Page_Object.create_success_account import create_success
import time
class create_successsaccount(unittest.TestCase):
    baseURL = "http://automationpractice.com/index.php"


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

    def test_create(self):
        lp = create_success(self.driver)
        mail = "nguyenhuydung14568@gmail.com"
        password = "123456"
        lp.click_signin()
        lp.set_emailaddress(mail)
        lp.set_textbox_password(password)
        lp.click_signinn()
        time.sleep(10)
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
