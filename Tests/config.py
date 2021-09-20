import errno

from selenium import webdriver
import time
import os
import unittest


class Test_session(unittest.TestCase):
    @classmethod
    # preconditions
    def setUp(self):
        project_root = os.path.dirname(os.path.dirname(__file__))

        # joining drivers with project root
        driver_path = os.path.join(project_root, "drivers")
        # getting chrome driver
        chrome_path = os.path.join(driver_path, "chromedriver.exe").replace("\\", "/")
        self.driver = webdriver.Chrome(executable_path=chrome_path)
        self.driver.maximize_window()

    def screen_shot(self, tc_step):
        SAVE_SCREENSHOTS = True
        SCREENSHOTS_ROOT = os.getcwd() + "/output/report/screenshot/"
        if not SAVE_SCREENSHOTS:
            return

        # self.id() returns something like "module.module.ClassName.test_method"
        base_path = os.path.join(SCREENSHOTS_ROOT, self.id().replace("\\", "/"))
        try:
            os.makedirs(base_path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(base_path):
                pass
            else:
                raise
        self.driver.save_screenshot(
            os.path.join(
                base_path,
                "{:02d}_{}.png".format(self.screenshot_counter, tc_step.replace(" ", "_")),
            )
        )
        self.screenshot_counter += 1

    # def setUp(self):
    #     super(Test_session, self).setUp()
    #     self.screenshot_counter = 0
    # E:\Calendar_Project\drivers\chromedriver.exe
    @classmethod
    # post
    def tearDown(self):
        self.driver.quit()

