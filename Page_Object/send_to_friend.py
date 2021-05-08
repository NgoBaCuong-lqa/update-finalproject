from Locators.Locator import send_to_friend
class Send_to_friends(send_to_friend):

    def __init__(self, driver):
        self.driver = driver

    def click_img(self):
        self.driver.find_element_by_xpath(self.img2).click()

    def click_button_send_to_friend(self):
        self.driver.find_element_by_xpath(self.button_send_to_friend).click()
    def setfriendname(self,friend_name):
        self.driver.find_element_by_xpath(self.textbox_friendname).send_keys(friend_name)
    def setemailaddress(self,emailaddress):
        self.driver.find_element_by_xpath(self.textbox_email_address).send_keys(emailaddress)
    def click_send(self):
        self.driver.find_element_by_xpath(self.button_send).click()