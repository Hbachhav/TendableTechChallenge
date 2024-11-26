from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ContactUsPage(BasePage):
    EMAIL_FIELD = (By.ID, "email")
    FIRST_NAME_FIELD = (By.ID, "firstname")
    LAST_NAME_FIELD = (By.ID, "lastname")
    COMPANY_FIELD = (By.ID, "company")
    MESSAGE_FIELD = (By.ID, "message")
    TYPE_DROPDOWN = (By.ID, "message_type")
    SUBMIT_BUTTON = (By.XPATH, "//div[@class='margin-top margin-small']//button[@type='submit'][normalize-space("
                               ")='Submit']")
    ERROR_MESSAGE = (By.XPATH, "//div[text()='Form Submission Failed']")

    def fill_contact_form(self, department, name, email, message=""):
        self.input_text(self.DEPARTMENT_DROPDOWN, department)
        self.input_text(self.NAME_FIELD, name)
        self.input_text(self.EMAIL_FIELD, email)
        if message:
            self.input_text(self.MESSAGE_FIELD, message)
        self.click(self.SUBMIT_BUTTON)

    def is_error_message_visible(self):
        return self.is_element_visible(self.ERROR_MESSAGE)
