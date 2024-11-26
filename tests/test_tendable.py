import pytest
from utils.driver_factory import DriverFactory
from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage


@pytest.fixture(scope="class")
def setup():
    """
    Fixture to set up and tear down the WebDriver.
    """
    driver = DriverFactory.get_driver()
    driver.get("https://www.tendable.com")
    yield driver
    driver.quit()


def test_menu_accessibility(setup):
    """
    Test to verify that the menus are accessible, clickable, and their corresponding content loads.
    """
    home_page = HomePage(setup)
    menus = ["About", "Products", "Sectors", "Contact"]

    for menu in menus:
        # Verify menu is clickable
        assert home_page.is_menu_clickable(menu), f"Menu '{menu}' is not clickable."


def test_request_demo_button(setup):
    """
    Test to verify the 'Request a Demo' button is visible and functional (clickable).
    """
    home_page = HomePage(setup)

    # Verify the 'Request a Demo' button is visible and clickable
    assert home_page.is_demo_button_visible(), "'Request a Demo' button is missing on the home page."
    assert home_page.is_demo_button_clickable(), "'Request a Demo' button is disable on the home page."


def test_contact_form_validation(setup):
    """
    Test to validate that an error message appears when the 'Message' field is left empty in the Contact Us form.
    """
    contact_us_page = ContactUsPage(setup)
    contact_us_page.fill_contact_form(department="Marketing", name="John Doe", email="john.doe@example.com")
    assert contact_us_page.is_error_message_visible(), (
        "Error message not displayed when 'Message' field is left empty."
    )
