from selenium import webdriver

class DriverFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        if browser == "chrome":
            return webdriver.Chrome()
        elif browser == "firefox":
            return webdriver.Firefox()
        else:
            raise ValueError("Unsupported browser: " + browser)
