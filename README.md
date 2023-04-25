# Автоматизированные UI тесты для Яндекс.Диск
### технологии : Python, Pytest, Selenium, Allure.

## Устаноновка
1. Склонировать репозиторий проекта.
2. Установить python не ниже 3.8.
3. Установить зависимости, в папке проекта выполнить `pip install -r requirements.txt`.
4. Установить Java и Allure (https://docs.qameta.io/allure/#_get_started)

## Запуск тестов и вывод отчета в Allure
1. Запуск выполнения тестов со сбором отчетности для allure : 
- `pytest --alluredir=<allure_reports_dir> [options]>`
2. доступные опции (п.1) (!!! по умолчанию прописаны настройки для запуска тестов на DEV контуре 10.100.8.65 ):
- --headless=false(true) - безголовый режим, если true, тогда окно браузера не открывается во время выполения тестов,
- --app-url=https://disk.yandex.ru - урл Яндекс.Диск,
- --webdr-manager=true - по умолчанию используется менеджер для селениум вебдрайвер,
- --webdr-path=<C:\\Program Files\\chromedriver\\chromedriver> - путь до селениум веб драйвер (вместе с именем файла)