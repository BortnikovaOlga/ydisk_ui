import os
from os import getcwd
# import pyperclip
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    JS_DRAG_DROP = None

    def __init__(self, locator, driver):
        self.locator = locator
        self.driver: WebDriver = driver
        self.element: WebElement = None

    def search(self, wait_time=10) -> WebElement:
        self.element = WebDriverWait(self.driver, wait_time). \
            until(EC.presence_of_element_located(self.locator), message=f"Can't find element by locator {self.locator}")
        return self.element

    def is_search(self, wait_time=3):
        try:
            self.element = WebDriverWait(self.driver, wait_time). \
                until(EC.invisibility_of_element_located(self.locator))
            return True
        except TimeoutException:
            return False

    def to_be_clickable(self, wait_time=10):
        self.element = WebDriverWait(self.driver, wait_time). \
            until(EC.element_to_be_clickable(self.locator), message=f"Element not clickable {self.locator}")
        return self.element

    def find(self):
        self.element = self.driver.find_element(*self.locator)
        return self

    def is_find(self):
        try:
            self.driver.find_element(*self.locator)
            return True
        except NoSuchElementException:
            return False

    def is_not_search(self, wait_time=5):
        """с ожиданием исчезновения на странице."""
        try:
            WebDriverWait(self.driver, wait_time). \
                until(EC.invisibility_of_element_located(self.locator))
        except TimeoutException:
            return False
        return True

    def input(self, text):
        if text is not None:
            if isinstance(text, int):
                text = str(text)
            elif isinstance(text, float):
                text = str(text).replace(".", ",")
            self.search()
            self.element.send_keys(Keys.CONTROL+"A")
            self.element.send_keys(Keys.BACKSPACE)
            self.element.send_keys(text)

    def click(self, wait_time=10):
        try:
            self.to_be_clickable(wait_time=wait_time).click()
        except (ElementNotInteractableException, ElementClickInterceptedException):
            self.find()
            self.driver.execute_script("arguments[0].click()", self.element)
        return self

    def context_click(self, wait_time=10):
        ActionChains(self.driver).context_click(self.to_be_clickable(wait_time=wait_time)).perform()

    def double_click(self, wait_time=10):
        ActionChains(self.driver).double_click(self.to_be_clickable(wait_time=wait_time)).perform()

    def click_without_wait(self):
        self.find()
        self.element.click()

    def hover(self):
        ActionChains(self.driver).move_to_element(self.search()).perform()
        return self

    # def insert_from_clipboard(self, text):
    #     pyperclip.copy(text)
    #     self.click()
    #     ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    #     return self

    def have_text(self, text, wait_time=7):
        find_text = text if isinstance(text, str) else str(text) if text else ""
        try:
            res = WebDriverWait(self.driver, wait_time). \
                until(EC.text_to_be_present_in_element(self.locator, find_text))
        except TimeoutException:
            res = False
        return res

    def have_aria_valuenow(self, value, wait_time=5):
        """смотрится значение в атрибуте aria-valuenow."""
        find_value = value if isinstance(value, str) else str(value) if value else ""
        return WebDriverWait(self.driver, wait_time). \
            until(EC.text_to_be_present_in_element_attribute(self.locator, "aria-valuenow", find_value))

    def have_value(self, value, wait_time=7):
        find_value = value if isinstance(value, str) else str(value).replace('.', ',') if isinstance(value, float) \
            else str(value) if value else ""
        try:
            res = WebDriverWait(self.driver, wait_time).until(
                EC.text_to_be_present_in_element_value(self.locator, find_value))
        except TimeoutException:
            res = False
        return res

    def is_checked(self):
        el: WebElement = self.search()
        checked = el.get_attribute("aria-checked")
        return checked == "true" or checked is True

    def get_value(self):
        self.find()
        return self.element.get_attribute("value")

    def get_text(self):
        return self.search().text

    def disabled(self):
        return True if self.search().get_attribute("disabled") else False

    def drag_and_drop(self, target):
        self.search()
        target.search()
        if BaseElement.JS_DRAG_DROP is None:
            cwd = getcwd()
            while not str.endswith(cwd, "test_ui"):
                cwd = os.path.dirname(cwd)
            cwd = os.path.join(os.path.join(cwd, "src"), "js")
            BaseElement.JS_DRAG_DROP = open(os.path.join(cwd, 'drag-drop.js'), 'r').read()
        self.driver.execute_script(BaseElement.JS_DRAG_DROP, self.element, target.element)
