import json
from appium import webdriver
import time

# Load desired capabilities from file
with open("config/desired_caps.json", "r") as f:
    desired_caps = json.load(f)

# Connect to Appium server
print("Connecting to Appium...")
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

print("Connected App launched.")

# wait and then quit
time.sleep(3)
driver.quit()
