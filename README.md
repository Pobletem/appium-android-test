# Appium-Android-Test

This project demonstrates mobile test automation of Android apps by using Appium and Python. This project uses the official Android emulator from Android studio.

## Test Cases

1. **App Launches Successfully (Smoke Test)**  
   Verifies that the app loads and the main screen is visible.

2. **Navigate to Notification Page**  
   Taps the "App" entry then the "Notification" entry and confirms the next screen loads.

3. **Verify Notifications show up in the Android UI**  
   Pulls down the Android notification menu and checks to see it received the expected notification


## Requirements

- Python 3.11+
- Node.js (v22.9 used)
- Appium 2.x
- Appium Python Client
- Android SDK & Emulator
- An APK file (this project uses the [ApiDemos-debug APK](https://github.com/appium/appium/tree/master/packages/appium/sample-code/apps))