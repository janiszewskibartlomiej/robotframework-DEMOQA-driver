from instance import SELENIUM, webdriver
from elements import elements

class demo_qa:
    """Demo QA driver"""

    def __init__(self):
        self.selenium_qa = SELENIUM
        self.elements = elements()

    def open_browser(self):
        """Open Browser"""
        opt = webdriver.ChromeOptions()
        opt.add_argument("--start-maximized")
        opt.add_argument("--ignore-certificate-errors")
        self.selenium_qa.create_webdriver("Chrome", options=opt)
        self.selenium_qa.set_selenium_speed(1)
        self.selenium_qa.maximize_browser_window()

    def navigation_to_page(self):
        self.selenium_qa.go_to('https://demoqa.com')

    def close_browser(self):
        """Close Browser"""
        self.selenium_qa.close_browser()