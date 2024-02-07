from .base_page import BasePage

class HomePage(BasePage):
    def go(self):
        self.driver.get("https://bcncgroup.com/")