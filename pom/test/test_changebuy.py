from selenium import webdriver
import unittest
from Page_Object.change_buy import Changebuyy
import sys

sys.path.append(r"C:\My-Final-Project-main\FInalProjects")


# Test Case Thay Đổi Thông Tin Mua Hàng
class Changebuys(unittest.TestCase):
    baseURL = "http://automationpractice.com/index.php"

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

    def test_change_buy(self):
        lp = Changebuyy(self.driver)
        lp.hover_picture()
        lp.click_adddtocard1()
        self.driver.implicitly_wait(10)
        lp.click_continueshopping1()
        lp.hover_picture2()
        lp.click_addtocard2()
        lp.click_continueshopping2()
        lp.hover_picture3()
        lp.click_addtocard3()
        lp.click_continueshopping3()
        lp.hover_picture4()
        lp.click_addtocard4()
        lp.click_continueshopping4()
        lp.hover_picture5()
        lp.click_addtocard5()
        lp.click_proceedtocheckout()

    def tearDown(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()
