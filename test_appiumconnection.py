import json
from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

# Load desired capabilities from file
with open("config/desired_caps.json", "r") as f:
    desired_caps = json.load(f)

# Convert desired caps file to UiAutomator2Options
options = UiAutomator2Options().load_capabilities(desired_caps)

# Connect to Appium server
print("Connecting to Appium...")
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

print("Connected App launched.")

# wait and then quit
time.sleep(3)
driver.quit()
