from Locators.Locator import contactUs
from selenium.webdriver.support.select import Select


class contactus(contactUs):


    def __init__(self, driver):
        self.driver = driver

    def click_contactus(self):
        self.driver.find_element_by_xpath(self.button_ContactUs).click()

    def set_subject(self):
        elt = self.driver.find_element_by_id(self.subject)
        self.drp = Select(elt)
        self.drp.select_by_value('2')

    def set_email_address(self, email):
        self.driver.find_element_by_id(self.Email_address_id).send_keys(email)

    def acctach_file(self, file_upload):
        elm = self.driver.find_element_by_id(self.textboxt_attach_file_id)
        elm.send_keys(file_upload)

    def set_message(self, message):
        self.driver.find_element_by_id(self.textbox_message_id).send_keys(message)

    def click_send(self):
        self.driver.find_element_by_id(self.send_id).click()
