from selenium import webdriver
import unittest
from Page_Object.newsletter import newsletterr
import sys
import time
from parameterized import parameterized

sys.path.append("C:\My-Final-Project-main\FInalProjects")


class Letters(unittest.TestCase):
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
        mail_newslettter = 'ngobacuong21113@gmail.com'
        lp = newsletterr(self.driver)
        lp.clicknewsletter()
        lp.setnewsletter(mail_newslettter)
        lp.click_newletter()
        time.sleep(5)

    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
