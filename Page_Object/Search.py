from Locators.Locator import Searchall

class Searchss(Searchall):

    def __init__(self, driver):
        self.driver = driver

    def click_textboxt_search(self):
        self.driver.find_element_by_xpath(self.textboxt_search).click()

    def set_text_boxt_search(self, Dress):
        self.driver.find_element_by_xpath(self.textboxt_search).send_keys(Dress)

    def clear_text_boxt_search(self):
        self.driver.find_element_by_xpath(self.textboxt_search).clear()

    def click_button_search(self):
        self.driver.find_element_by_xpath(self.button_search).click()

    def kiemtragia(self):
        self.driver.find_element_by_xpath(self.price_product).text

    def kiemtradress(self):
        all_product = self.driver.find_elements_by_xpath(self.product)
        return all_product

