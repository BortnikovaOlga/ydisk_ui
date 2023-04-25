from selenium.webdriver.common.by import By


class AuthPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[href='https://passport.yandex.ru/auth?retpath=https%3A%2F%2Fdisk.yandex.ru']")
    YANDEX_ID_BUTTON = (By.CSS_SELECTOR, "a[aria-label='Войти через Яндекс ID']")

    LOGIN = (By.ID, "passp-field-login")
    SUBMIT = (By.ID, "passp:sign-in")

    PASSWORD = (By.ID, "passp-field-passwd")
    SKIP_EMAIL = (By.CSS_SELECTOR, "div[data-t='email_skip'] button")

    # USER_BUTTON = (By.CSS_SELECTOR, "div.header__username-wrapper button")
    # USER_MENU_EXIT = (By.XPATH, "//div[@id='popup_menu']//a[.='Выход']")
    # ERROR_MESSAGE = (By.CSS_SELECTOR, "div.p-message-wrapper span.p-message-detail")
    # EMPTY_LOGIN_MSG = (By.XPATH, '//small[.="Введите имя"]')
    # EMPTY_PASSWORD_MSG = (By.XPATH, '//small[.="Введите пароль"]')
