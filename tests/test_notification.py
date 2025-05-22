import json
import unittest
from appium import webdriver
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

class TestAppLaunch(unittest.TestCase):
    def setUp(self):
        # opens the desired caps file containing emulator capabilities
        with open('config/desired_caps.json') as f:
            # loads the json file into python dictionary
            desired_caps = json.load(f)
        # create appium options object using the file
        options = UiAutomator2Options().load_capabilities(desired_caps)
        # launches a remote webdriver session with appium
        self.driver = webdriver.Remote("http://localhost:4723", options=options)
        

    def test_app_notification(self):

        # need to naviagte the app to find notifications
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "App").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Notification").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "IncomingMessage").click()

        # check to see if we are in the right page after navigating
        el = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Show App Notification")
        self.assertIsNotNone(el, "Show App Notification section should be visible after launch")

        # click on show app notification
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Show App Notification").click()
        
        # open android notification
        self.driver.open_notifications()
        time.sleep(2) # wait a bit

        # check to see if notification from 'Joe' is not found
        notification = self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textContains("Joe")'
            )
        
        self.assertIsNotNone(notification, "Notification from 'Joe' not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
