class BasePage:
    def __init__(self, url, app):
        self.app = app
        self.url = url

    def open(self, object_link=None):
        url = self.url
        if object_link is not None:
            url += "/" + object_link
        self.app.driver.get(url)
        self.app.driver.maximize_window()

    def get_screenshot(self):
        return self.app.driver.get_screenshot_as_png()
