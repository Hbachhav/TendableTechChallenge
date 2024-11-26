from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from pages.base_page import BasePage


class HomePage(BasePage):
    MENU_ITEMS = {
        "About": (By.XPATH, "//a[@class='navbar7_link w-nav-link'][normalize-space()='About']"),
        "Products": (By.XPATH, "//a[@class='navbar7_link w-nav-link'][normalize-space()='Products']"),
        "Sectors": (By.XPATH, "//a[@class='navbar7_link w-nav-link'][normalize-space()='Sectors']"),
        "Contact": (By.XPATH, "//a[@class='navbar7_link w-nav-link'][normalize-space()='Contact']")
    }
    DEMO_BUTTON = (By.XPATH, "//a[normalize-space()='Book a demo']")

    def is_menu_clickable(self, menu_name):
        """
        Checks if the given menu item is visible, enabled, and ready to be clicked.
        """
        menu_locator = self.MENU_ITEMS.get(menu_name)
        if not menu_locator:
            raise ValueError(f"Menu '{menu_name}' not found in MENU_ITEMS")

        try:
            # Wait for the menu element to be visible and enabled
            element = self.wait_for_element(menu_locator)
            return element.is_displayed() and element.is_enabled()
        except TimeoutException:
            return False

    def navigate_to_menu(self, menu_name):
        """
        Navigates to the given menu item, ensuring it is clickable.
        """
        menu_locator = self.MENU_ITEMS.get(menu_name)
        if not menu_locator:
            raise ValueError(f"Menu '{menu_name}' not found in MENU_ITEMS")

        try:
            # Ensure the element is clickable
            if not self.is_menu_clickable(menu_name):
                raise Exception(f"Menu '{menu_name}' is not clickable.")
            self.click(menu_locator)
        except ElementClickInterceptedException:
            # Fallback to JavaScript click if direct click fails
            self.click_via_js(menu_name)

    def click_via_js(self, menu_name):
        """
        Clicks the menu item using JavaScript as a fallback.
        """
        menu_locator = self.MENU_ITEMS.get(menu_name)
        if not menu_locator:
            raise ValueError(f"Menu '{menu_name}' not found in MENU_ITEMS")

        element = self.wait_for_element(menu_locator)
        self.driver.execute_script("arguments[0].click();", element)

    def is_demo_button_visible(self):
        """
        Checks if the 'Request a Demo' button is visible on the page.
        """
        try:
            return self.is_element_visible(self.DEMO_BUTTON)
        except TimeoutException:
            return False

    def is_demo_button_clickable(self):
        try:
            return self.is_element_clickable(self.DEMO_BUTTON)
        except TimeoutException:
            return False
