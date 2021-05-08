from Locators.Locator import newsletter
class newsletterr(newsletter):


    def __init__(self, driver):
        self.driver = driver

    def clicknewsletter(self):
        self.driver.find_element_by_xpath(self.textbox_newsletter_xpath).click()

    def setnewsletter(self,email_newsletter):
        self.driver.find_element_by_xpath(self.textbox_newsletter_xpath).send_keys(email_newsletter)

    def click_newletter(self):
        self.driver.find_element_by_xpath(self.button_newsletter).click()