from .base_page import BasePage

class WhoWeArePage(BasePage):
    def go(self):
        self.driver.get("https://bcncgroup.com/who-we-are/")