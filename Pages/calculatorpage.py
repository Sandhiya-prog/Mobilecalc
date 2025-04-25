from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def tap_digit(self, num):
        digit_locator = (AppiumBy.ID, f"com.vivo.calculator:id/digit_{num}")
        self._click(digit_locator)

    def tap_operator(self, operator):
        operator_locator = {
            '+': (AppiumBy.ACCESSIBILITY_ID, "Plus"),
            '-': (AppiumBy.ACCESSIBILITY_ID, "Minus"),
            '*': (AppiumBy.ACCESSIBILITY_ID, "Multiply"),
            '/': (AppiumBy.ACCESSIBILITY_ID, "Divide")
        }
        self._click(operator_locator[operator])

    def equals(self):
        equal_btn = (AppiumBy.ACCESSIBILITY_ID, "=")
        self._click(equal_btn)

    def result(self):
        result_locator = (AppiumBy.ID, "com.vivo.calculator:id/formula")
        result_element = self.wait.until(EC.presence_of_element_located(result_locator))
        return result_element.text