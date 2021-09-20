# from selenium import webdriver
# from selenium.common import exceptions
# from selenium.common.exceptions import TimeoutException
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver import ActionChains
# import time
# # url = "https://demoqa.com/droppable/"
#
# url = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
# driver = webdriver.Chrome(executable_path="E:/Calendar_Project/drivers/chromedriver.exe")
# driver.get(url)
# #
# # driver.maximize_window()
# # source= driver.find_element_by_id("draggable")
# # target= driver.find_element_by_id("droppable")
# # actionchainvar = ActionChains(driver)
# # actionchainvar.drag_and_drop(source,target).perform()
#
#
# # driver = webdriver.Chrome()
# # driver.get(url)
# # driver.maximize_window()
# # action = ActionChains(driver)
# # time.sleep(5)
# # element = driver.find_element_by_xpath("//a[normalize-space()='Progress Bars']")
# # time.sleep(5)
# # action.move_to_element(element).click(element).perform()
# # driver.close()
#
# # #Click
# # driver.maximize_window()
# # action = ActionChains(driver)
# # time.sleep(5)
# # elements = driver.find_element_by_link_text("Alerts & Modals")
# # time.sleep(5)
# # action.move_to_element(elements).click(elements).perform()
# # driver.close()
#
# # #Click and hold
# # driver.maximize_window()
# # action = ActionChains(driver)
# # time.sleep(5)
# # elements = driver.find_element_by_link_text("Alerts & Modals")
# # time.sleep(5)
# # action.click_and_hold(on_element = elements).perform()
#
#
# #right click
# # driver.maximize_window()
# # action = ActionChains(driver)
# # time.sleep(5)
# # elements = driver.find_element_by_link_text("Alerts & Modals")
# # time.sleep(5)
# # action.context_click(on_element = elements).perform()
#
# #double  click
# driver.maximize_window()
# action = ActionChains(driver)
# time.sleep(5)
# elements = driver.find_element_by_link_text("Alerts & Modals")
# time.sleep(5)
# action.double_click(on_element = elements).perform()
#
#
# #double  click
# driver.maximize_window()
# action = ActionChains(driver)
# time.sleep(5)
# elements = driver.find_element_by_link_text("Alerts & Modals")
# time.sleep(5)
# action.double_click(on_element = elements).perform()
#
#
# # action.move_to_element(elements).click(elements).perform()
# driver.close()
#
#
# # try:
# #     a = 5
# #     b = 0
# #     c = a / b
# #     print(c)
# # except ZeroDivisionError:
# #     print("Infinity")
#
#
#
# # try:
# #     self.find_element(locator=locator).is_present()
# #     return True
# # except TimeoutException:
# #     return False
#
#
# # try:
# #     myElem = WebDriverWait(self.driver, delay).until( EC.presence_of_element_located((locator)) )
# #     return myElem
# # except ( exceptions.NoSuchElementException, exceptions.StaleElementReferenceException, exceptions.TimeoutException, ):
# #     return sync_notification_appeared
