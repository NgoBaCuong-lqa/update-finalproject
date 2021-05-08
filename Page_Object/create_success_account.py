class create_success():
    button_Sign_xpath = '//a[@class="login"]'

    button_Createanaccount = "SubmitCreate"
    textbox_email = '//*[@id="email"]'
    textbox_password = '//*[@id="passwd"]'
    button_signinregister = '//*[@id="SubmitLogin"]'

    def __init__(self, driver):
        self.driver = driver

    def click_signin(self):
        self.driver.find_element_by_xpath(self.button_Sign_xpath).click()

    def set_emailaddress(self, email):
        self.driver.find_element_by_xpath(self.textbox_email).send_keys(email)

    def set_textbox_password(self, password):
        self.driver.find_element_by_xpath(self.textbox_password).send_keys(password)
    def click_signinn(self):
        self.driver.find_element_by_xpath(self.button_signinregister).click()
