# Tendable Test Automation

Overview
This project automates key tests for the Tendable website using Python and Selenium. The primary focus is on verifying navigation menus, the "Request a Demo" button functionality, and form validation on the "Contact Us" page. The Page Object Model (POM) design pattern is employed for maintainability and scalability.

How to Run
1. Clone the Repository
Open your terminal or PyCharm terminal and clone the repository using the following command:

bash
Copy code
git clone https://github.com/Hbachhav/TendableTechChallenge.git
2. Open the Project in PyCharm
Launch PyCharm and click on File > Open.
Navigate to the cloned folder (TendableTechChallenge) and select it.
Wait for PyCharm to index the project.
3. Install Dependencies
In the PyCharm terminal, run:

bash
Copy code
pip install -r requirements.txt
4. Run the Tests
Execute the following command in the PyCharm terminal to run all tests:

bash
Copy code
pytest tests/
Alternatively, you can right-click the tests folder in the PyCharm project view and select Run 'pytest in tests'.


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
