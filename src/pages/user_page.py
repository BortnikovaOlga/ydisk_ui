import allure

from src.elements.base_element import BaseElement
from src.locators.user_page_locators import UserPageLocators
from src.pages.base_page import BasePage


class UseDiskPage(BasePage):

    def __init__(self, url, app):
        """
        Страница клиента Яндекс.Диск
        """
        super().__init__(url, app)
        self.files = BaseElement(UserPageLocators.FILES, app.driver)
        self.create = BaseElement(UserPageLocators.CREATE_NEW_BUTTON, app.driver)
        self.create_folder_i = BaseElement(UserPageLocators.CREATE_FOLDER, app.driver)
        self.folder_name = BaseElement(UserPageLocators.FOLDER_NAME_INPUT, app.driver)
        self.submit_create = BaseElement(UserPageLocators.CREATE_SUBMIT_BUTTON, app.driver)
        self.copy = BaseElement(UserPageLocators.COPY_BUTTON, app.driver)
        self.copy_submit = BaseElement(UserPageLocators.DIALOG_SUBMIT_BUTTON, app.driver)
        self.user_menu = BaseElement(UserPageLocators.USER_MENU, app.driver)
        self.user_logout = BaseElement(UserPageLocators.USER_LOGOUT, app.driver)

    @allure.step("Создать папку.")
    def create_folder(self, name: str):
        """Создать папку с именем из name.
        Выполнить : кнопка Создать, выбрать Создать папку, ввести имя папки, нажать Сохранить."""
        self.create.click()
        self.create_folder_i.click()
        self.folder_name.input(name)
        self.submit_create.click()
        return self

    def file_or_folder_element(self, file):
        return BaseElement(UserPageLocators.file(file), self.app.driver)

    @allure.step("Скопировать файл в папку.")
    def copy_file_to_folder(self, file, folder):
        """Скопировать файл file из корня в папку folder.
        Выполнить : переход в корень, вызвать контекстное меню файла (правой кнопкой мыши), в меню выбрать Копировать,
        выбрать папку назначения, нажать Копировать."""
        self.files.click()
        self.file_or_folder_element(file).context_click()
        self.copy.click()
        target_folder = BaseElement(UserPageLocators.target_folder(folder), self.app.driver)
        target_folder.click()
        self.copy_submit.click()
        return self

    @allure.step("Проверить наличие файла в папке.")
    def file_in_folder(self, file, folder) -> bool:
        """Возвращает true, если в папке folder есть файл file.
        Выполнить : переход в корень, зайти в папку двойным кликом, проверить наличие файла."""
        self.files.click()
        self.file_or_folder_element(folder).double_click()
        return self.file_or_folder_element(file).is_search()

    @allure.step("Выход из ЛК")
    def logout(self):
        self.user_menu.click()
        self.user_logout.click()
