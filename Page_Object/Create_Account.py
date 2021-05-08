from Locators.Locator import Create_account
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Account(Create_account):

    def __init__(self, driver):
        self.driver = driver

    def click_signin(self):
        self.driver.find_element_by_xpath(self.button_Signin_xpath).click()

    def set_emailaddress(self, email):
        self.driver.find_element_by_id(self.textbox_emailcreate_id).send_keys(email)

    def click_createanaccount(self):
        button_Createanaccount_elm = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.button_Createanaccount))
        )
        button_Createanaccount_elm.click()
