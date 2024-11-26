from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def input_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.send_keys(text)

    def is_element_visible(self, locator):
        try:
            self.wait_for_element(locator)
            return True
        except:
            return False

    def is_element_clickable(self, locator):
        """Check if an element is clickable (visible and enabled)."""
        try:
            # Wait for the element to be clickable (visible and enabled)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except TimeoutException:
            return False
