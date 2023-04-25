from src.app.page_factory import PageFactory, Pages


class Application:
    def __init__(self, driver, app_url):
        self.driver = driver
        self.url = app_url
        # self.url = f'http://{app_host}' if app_port is None else f'http://{app_host}:{app_port}'
        # self.host = app_host
        # self.port = app_port

        self.__page_factory = PageFactory(app=self)

    def get_page(self, page_type: Pages):
        return self.__page_factory.get_page(page_type)

    def quit(self):
        self.driver.quit()

    def get_screenshot(self):
        return self.driver.get_screenshot_as_png()
