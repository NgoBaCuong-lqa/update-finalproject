from selenium import webdriver
import unittest
from Page_Object.newsletter import newsletterr
import sys
import time

sys.path.append("C:\My-Final-Project-main\FInalProjects")


class Letter(unittest.TestCase):
    email_newsletter = 'ngobacuong2113@gmail.com'

    baseURL = "http://automationpractice.com/index.php"
    driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

    def test_newsletter(self):
        lp = newsletterr(self.driver)
        lp.clicknewsletter()
        lp.setnewsletter(self.email_newsletter)
        lp.click_newletter()
        time.sleep(5)

        # if self.driver.find_element_by_xpath('//*[@id="columns"]/div[1]'):
        #     self.assertTrue(True)
        # else:
        #     self.assertFalse(False)

    def tearDown(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()