#Can reuse for all projects
#Contains all actions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.common import exceptions
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

class webActionClassOne(unittest.TestCase) :
    def __init__(self, driver):
        self.driver = driver

    def type (self ,locator,text):
        WebDriverWait (self.driver , 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def click (self ,locator):
        WebDriverWait (self.driver , 10).until(EC.element_to_be_clickable(locator)).click()

    def choose (self ,locator,text):
        element = Select(WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)))
        element.select_by_visible_text(text)

    def getUrl (self ,url):
        self.driver.get(url)

    def getText (self,locator):
        get_Text = WebDriverWait (self.driver , 10).until(EC.visibility_of_element_located(locator))
        return get_Text.text

    def find_element(self,locator):
        self.driver.find_element(locator)

    def page_load(self, locator):
        sync_notification_appeared = False
        delay = 10
        try:
            myElem = WebDriverWait(self.driver, delay).until(
                EC.presence_of_element_located((locator))
            )
            return myElem
        except (
                exceptions.NoSuchElementException,
                exceptions.StaleElementReferenceException,
                exceptions.TimeoutException,
        ):
            return sync_notification_appeared

    def clear(self, locator):

        clearelement = self.find_clickable_element(locator)
        clearelement.clear()
        return clearelement

        # if element is not None:
        #     return element.find_element(locator)
        # elif explicit_wait:
        #     return self.explicit_wait.until(EC.visibility_of_element_located(locator))
        # else:

    # def getTexts(self, locator):
    #         get_Texts = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    #         return get_Texts.text

        # driver.find_element_by_xpath("//input[@name='password']").send_keys('ram')

