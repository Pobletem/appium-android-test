import json
import unittest
from appium import webdriver
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

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
        

    def test_app_launches(self):
        # Check that the app loads and the home screen has a known element
        # Attempts to find element named App
        el = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "App")
        # If element is found then assertion passes, else fails
        self.assertIsNotNone(el, "App section should be visible after launch")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
