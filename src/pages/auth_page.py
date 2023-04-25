import logging.config

import allure

from src.elements.base_element import BaseElement
from src.locators.auth_page_locators import AuthPageLocators
from src.models.auth import AuthData
from src.pages.base_page import BasePage

logger = logging.getLogger("tz_ui")


class AuthPage(BasePage):

    def __init__(self, url, app):
        super().__init__(url, app)
        self.login = BaseElement(AuthPageLocators.LOGIN, app.driver)
        self.password = BaseElement(AuthPageLocators.PASSWORD, app.driver)
        self.submit = BaseElement(AuthPageLocators.SUBMIT, app.driver)

    @allure.step("Авторизация.")
    def auth(self, data: AuthData):
        logger.info(f"Login with username={data.login} password={data.password}")
        self.login.input(data.login)
        self.submit.click()
        self.password.input(data.password)
        self.submit.click()
