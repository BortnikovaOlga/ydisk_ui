from selenium.webdriver.common.by import By


class UserPageLocators:
    FILES = (By.ID, "/disk")
    CREATE_NEW_BUTTON = (By.CSS_SELECTOR, "span.create-resource-popup-with-anchor button")

    CREATE_FOLDER = (By.CSS_SELECTOR, "div.create-resource-popup-with-anchor__create-items button[aria-label='Папку']")
    FOLDER_NAME_INPUT = (By.CSS_SELECTOR, "div.dialog__body input")
    CREATE_SUBMIT_BUTTON = (By.CSS_SELECTOR, "div.dialog__body button")

    COPY_BUTTON = (By.CSS_SELECTOR, "div.resources-actions-popup__wrapper div[value='copy']")
    DIALOG_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.confirmation-dialog__button_submit")

    USER_MENU = (By.CSS_SELECTOR, "a[aria-label='Аккаунт']")
    USER_LOGOUT = (By.CSS_SELECTOR, "a[aria-label='Выйти из аккаунта']")

    @staticmethod
    def file(name: str):
        return By.CSS_SELECTOR, f"div.listing-item__info div[aria-label='{name}']"

    @staticmethod
    def target_folder(name: str):
        return By.XPATH, f"//div[@class='dialog__body']//div[contains(@aria-label, '{name}')]"
