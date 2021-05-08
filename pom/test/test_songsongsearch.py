from selenium import webdriver
import unittest
from Page_Object.Search import Searchss
from parameterized import parameterized
import sys
import time

sys.path.append(r"C:\My-Final-Project-main\FInalProjects")


class SearchTest(unittest.TestCase):
    baseURL = "http://automationpractice.com/index.php"

    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    def test_search(self, browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome(executable_path=r"C:\Driver\chromedriver.exe")
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"C:\Driver\geckodriver.exe")
            time.sleep(3)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        lp = Searchss(self.driver)
        Dress = "Dress"
        lp.click_textboxt_search()
        lp.set_text_boxt_search(Dress)
        lst = lp.kiemtradress()
        time.sleep(5)

        for elm in lst:
            elm_text = elm.text
            self.assertIn("Dress", elm_text, 'False')

    @parameterized.expand([
        ["Chrome"],
        ["Firefox"],
    ])
    def test_search3(self, browser):
        if browser == "Chrome":
            self.driver = webdriver.Chrome(executable_path=r"C:\Driver\chromedriver.exe")
            time.sleep(3)
        elif browser == "Firefox":
            self.driver = webdriver.Firefox(executable_path=r"C:\Driver\geckodriver.exe")
            time.sleep(3)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
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
