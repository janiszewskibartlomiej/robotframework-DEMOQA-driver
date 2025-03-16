from instance import SELENIUM
from xpath import xpath


class text_box():

    def navigation_to_page(self):
        SELENIUM.click_element(xpath.xpath_text_box)

    def input_text(self, xpath, val):
        SELENIUM.input_text(xpath, val)

    def click_button(self, xpath):
        SELENIUM.execute_javascript(("window.scrollTo(10000, 10000)"))
        SELENIUM.click_element(xpath)

    def input_name(self, value):
        SELENIUM.input_text(xpath.xpath_text_box_name, value)

    def click_submit_button(self):
        SELENIUM.execute_javascript(("window.scrollTo(10000, 10000)"))
        SELENIUM.click_element(xpath)