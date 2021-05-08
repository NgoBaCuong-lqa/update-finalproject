from selenium import webdriver
import unittest
from Page_Object.Search import Searchss
# import HtmlTestRunner
import sys

import time

sys.path.append(r"C:\My-Final-Project-main\FInalProjects")


class Searchs(unittest.TestCase):
    baseURL = "http://automationpractice.com/index.php"


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

    def test_search(self):
        Dress = "Dress"
        lp = Searchss(self.driver)
        lp.click_textboxt_search()
        lp.set_text_boxt_search(Dress)
        time.sleep(5)
        lp.clear_text_boxt_search()
        time.sleep(5)

    def test_search2(self):
        Dress = "Dress"
        lp = Searchss(self.driver)
        lp.click_textboxt_search()
        lp.set_text_boxt_search(Dress)
        lst = lp.kiemtradress()
        time.sleep(5)

        for elm in lst:
            elm_text = elm.text
            self.assertIn("Dress", elm_text, 'False')

    def test_search3(self):
        Dress = "Dress"
        lp = Searchss(self.driver)
        lp.click_textboxt_search()
        lp.set_text_boxt_search(Dress)
        lp.click_button_search()
        lp.kiemtragia()
        time.sleep(5)

        self.assertNotEqual(' ', lp.price_product, "fail")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
