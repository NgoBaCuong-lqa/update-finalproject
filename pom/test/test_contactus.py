from selenium import webdriver
import unittest
from Page_Object.ContactUs import contactus
import sys
import time

sys.path.append(r"C:\Users\Admin\PycharmProjects\UpdateFinalproject")


class Contactus(unittest.TestCase):
    baseURL = "http://automationpractice.com/index.php"


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

    def test_contactus(self):
        email = "nguyenhuydung14568@gmail.com"
        message = "123456"
        file_upload = r'C:/Users/New folder/Xpath.txt'

        lp = contactus(self.driver)
        lp.click_contactus()
        lp.set_subject()
        lp.set_email_address(email)
        lp.set_message(message)
        lp.acctach_file(file_upload)
        lp.click_send()
        time.sleep(5)
        if self.driver.find_element_by_xpath("/html/head/title"):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def tearDown(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()
