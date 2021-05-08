from Locators.Locator import Chitietsanpham
class Chitietsanphams( Chitietsanpham):

    def __init__(self, driver):
        self.driver = driver

    def click_img3(self):
        self.driver.find_element_by_xpath(self.img1).click()

    def click_product(self):
        self.driver.find_element_by_xpath(self.product_xpath).click()
