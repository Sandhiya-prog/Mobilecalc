from appium import webdriver
from appium.options.android import UiAutomator2Options
from Pages.calculatorpage import CalculatorPage

def before_all(context):
    # Create an AppiumOptions object
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("platformVersion", "14")  # Ensure this matches your device version
    options.set_capability("deviceName", "10BCCY1FZQ0014K")  # Device ID from adb devices
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("appPackage", "com.vivo.calculator")
    options.set_capability("appActivity", "com.vivo.calculator.Calculator")
    options.set_capability("noReset", True)  # This will prevent resetting app data between sessions

    try:
        # Initialize the Appium driver using the AppiumOptions object
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub" , options=options)
        driver.implicitly_wait(10)  # Set an implicit wait for finding elements
        context.driver=driver

        # Initialize the page object
        context.calculatorpage = CalculatorPage(context.driver)

    except Exception as e:
        print(f"Error initializing driver: {e}")
        raise Exception("Failed to initialize Appium driver")
