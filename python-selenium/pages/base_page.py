class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go(self):
        pass

    def get_title(self):
        return self.driver.title