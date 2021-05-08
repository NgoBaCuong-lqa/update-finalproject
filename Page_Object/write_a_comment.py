from Locators.Locator import write_a_comment
from selenium.webdriver import ActionChains


class write_a_comments(write_a_comment):

    def __init__(self, driver):
        self.driver = driver

    def click_signin(self):
        self.driver.find_element_by_xpath(self.button_Signin_xpath).click()

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.textboxt_email_address).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.textbox_password).send_keys(password)

    def click_signin_register(self):
        self.driver.find_element_by_xpath(self.button_signin_register).click()

    def click_img_logo(self):
        self.driver.find_element_by_xpath(self.img_logo).click()

    def hover_picture1(self):
        picture1_xpath = '//*[@id="homefeatured"]/li[1]'
        picture1 = self.driver.find_element_by_xpath(picture1_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(picture1).perform()

    def click_img1(self):
        self.driver.find_element_by_xpath(self.img1).click()

    def click_button_write_a_review(self):
        self.driver.find_element_by_xpath(self.button_write_a_review).click()

    def set_title(self, title):
        self.driver.find_element_by_id(self.textboxt_title_id).send_keys(title)

    def set_comment(self, comment):
        self.driver.find_element_by_xpath(self.text_comment).send_keys(comment)

    def click_send(self):
        self.driver.find_element_by_xpath(self.button_send).click()
