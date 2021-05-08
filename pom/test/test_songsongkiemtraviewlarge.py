from selenium import webdriver
import unittest
from Page_Object.kiemtraviewlarge import Chitietsanphams
import sys
import time
from parameterized import parameterized

sys.path.append("C:\My-Final-Project-main\FInalProjects")


class ChiTietSanPham(unittest.TestCase):
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
        lp = Chitietsanphams(self.driver)
        lp.click_img3()
        time.sleep(5)
        lp.click_product()
        time.sleep(5)

    def tearDown(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()
