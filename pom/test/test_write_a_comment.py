from selenium import webdriver
import unittest
from Page_Object.write_a_comment import write_a_comments
import sys
import time

sys.path.append("C:\My-Final-Project-main\FInalProjects")


class Writeacomment(unittest.TestCase):
    baseURL = "http://automationpractice.com/index.php"

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

    def test_write_a_comment(self):
        email = 'nguyenhuydung14568@gmail.com'
        password = '123456'
        title = 'beautiful clothes'
        comment = '123'

        lp = write_a_comments(self.driver)
        lp.click_signin()
        lp.set_email(email)
        lp.set_password(password)
        lp.click_signin_register()
        time.sleep(5)
        lp.click_img_logo()
        time.sleep(2)
        lp.hover_picture1()
        lp.click_img1()
        self.driver.implicitly_wait(10)
        lp.click_button_write_a_review()
        lp.set_title(title)
        lp.set_comment(comment)
        lp.click_send()
        time.sleep(5)

    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
