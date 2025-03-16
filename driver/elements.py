from instance import SELENIUM


class elements:

    def naigation_to_page(self):
        import time
        time.sleep(10)
        SELENIUM.click_element('//*[@id="app"]/div/div/div[2]/div/div[1]')
