# Tendable Test Automation

Overview
This project automates key tests for the Tendable website using Python and Selenium. The primary focus is on verifying navigation menus, the "Request a Demo" button functionality, and form validation on the "Contact Us" page. The Page Object Model (POM) design pattern is employed for maintainability and scalability.

# How to Run
Clone the Repository:
https://github.com/Hbachhav/TendableTechChallenge.git

bash
Copy code
git clone https://github.com/Hbachhav/TendableTechChallenge.git

#Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Tests:

bash
Copy code
pytest tests/
# Strategy
Page Object Model (POM):

Created reusable page classes (HomePage, ContactUsPage) to encapsulate locators and actions.
Test Cases:

Verified menu clickability and navigation.
Checked for "Request a Demo" button visibility and functionality.
Tested form validation with an empty "Message" field.
Assertions:

Used dynamic checks for element visibility and clickability.
Ensured appropriate error messages display for invalid form submissions.
