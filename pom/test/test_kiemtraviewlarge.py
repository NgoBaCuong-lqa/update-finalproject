from selenium import webdriver
import unittest
from Page_Object.kiemtraviewlarge import Chitietsanphams
import sys
import time

sys.path.append("C:\My-Final-Project-main\FInalProjects")


class TestChiTietSanPham(unittest.TestCase):
    baseURL = "http://automationpractice.com/index.php"
    driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

    def test_chitietsanpham(self):
        lp = Chitietsanphams(self.driver)
        lp.click_img3()
        time.sleep(5)
        lp.click_product()
        time.sleep(5)


def tearDown(cls):
    cls.driver.close()


if __name__ == '__main__':
    unittest.main()
