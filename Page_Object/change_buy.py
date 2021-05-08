from selenium.webdriver import ActionChains
from Locators.Locator import changebuy


class Changebuyy(changebuy):

    def __init__(self, driver):
        self.driver = driver


    def hover_picture(self):
        picture1_xpath = '//*[@id="homefeatured"]/li[1]'
        picture1 = self.driver.find_element_by_xpath(picture1_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(picture1).perform()

    def click_adddtocard1(self):
        self.driver.find_element_by_xpath(self.button_addtocard1).click()

    def click_continueshopping1(self):
        self.driver.find_element_by_xpath(self.button_continue_shopping).click()

    def hover_picture2(self):
        picture2_xpath = '//*[@id="homefeatured"]/li[2]'
        picture2 = self.driver.find_element_by_xpath(picture2_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(picture2).perform()

    def click_addtocard2(self):
        self.driver.find_element_by_xpath(self.button_addtocard2).click()

    def click_continueshopping2(self):
        self.driver.find_element_by_xpath(self.button_continue_shopping).click()

    def hover_picture3(self):
        picture3_xpath = '//*[@id="homefeatured"]/li[3]'
        picture3 = self.driver.find_element_by_xpath(picture3_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(picture3).perform()

    def click_addtocard3(self):
        self.driver.find_element_by_xpath(self.button_addtocard3).click()

    def click_continueshopping3(self):
        self.driver.find_element_by_xpath(self.button_continue_shopping).click()

    def hover_picture4(self):
        picture4_xpath = '//*[@id="homefeatured"]/li[4]'
        picture4 = self.driver.find_element_by_xpath(picture4_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(picture4).perform()

    def click_addtocard4(self):
        self.driver.find_element_by_xpath(self.button_addtocard4).click()

    def click_continueshopping4(self):
        self.driver.find_element_by_xpath(self.button_continue_shopping).click()

    def hover_picture5(self):
        picture5_xpath = '//*[@id="homefeatured"]/li[5]'
        picture5 = self.driver.find_element_by_xpath(picture5_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(picture5).perform()

    def click_addtocard5(self):
        self.driver.find_element_by_xpath(self.button_addtocard5).click()

    def click_proceedtocheckout(self):
        self.driver.find_element_by_xpath(self.button_proceedtocheckout).click()
