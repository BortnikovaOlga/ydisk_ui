from enum import Enum

from src.pages.auth_page import AuthPage
from src.pages.user_page import UseDiskPage


class Pages(Enum):
    """Типы страниц. В значениях класс этой страницы."""
    AUTH_PAGE = AuthPage
    USER_DISK_PAGE = UseDiskPage


"""Path к странице."""
PAGE_PATH = {
    Pages.AUTH_PAGE: "https://passport.yandex.ru/auth?retpath=https%3A%2F%2Fdisk.yandex.ru",
    Pages.USER_DISK_PAGE: "https://disk.yandex.ru/client/disk"
    }


class PageFactory:
    """Фабрика страниц."""

    def __init__(self, app):
        """ app : приложение для которого создается фабрика, передается аргументом в созданные страницы."""
        self.pages = {}
        self.app = app

    def get_page(self, page_type: Pages):
        """возвращает страницу указанного типа, если она хранится в словаре страниц,
         иначе создает новую и сохраняет в словарь pages."""
        if page_type in self.pages:
            return self.pages[page_type]
        else:
            page = page_type.value(url=PAGE_PATH[page_type], app=self.app)
            self.pages[page_type] = page
            return page
