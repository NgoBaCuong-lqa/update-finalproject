from Locators.Locator import share_to_tweet
class share_to_tweets(share_to_tweet):

    def __init__(self, driver):
        self.driver = driver

    def click_img2(self):
        self.driver.find_element_by_xpath(self.image2).click()

    def click_tweet(self):
        self.driver.find_element_by_xpath(self.button_tweet).click()
