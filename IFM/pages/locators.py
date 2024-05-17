from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN = (By.CSS_SELECTOR, "input[id='username']")
    PASSWORD = (By.CSS_SELECTOR, "input[id='password']")
    CONFIRMATION_CODE = (By.CSS_SELECTOR, "input[id='code']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    WRONG_MESSAGE = (By.CSS_SELECTOR, "div[class='ant-alert-message']")
    CHECKBOX_NOT_LOGGING_OUT = (By.CSS_SELECTOR, "input[id='notLoggingOut']")

class MainPageLocators():
    STATISTICS = (By.LINK_TEXT, "Статистика")
    DEAL = (By.LINK_TEXT, "Сделки")
    CHAT = (By.LINK_TEXT, "Чат")
    REPORTS = (By.CSS_SELECTOR, "img[src = '/assets/reports-44e0922c.png']")
    PROFITS = (By.XPATH,"//a[text()='Прибыль и убытки']")
    INVESTORS_PORTFOLIO = (By.XPATH,"//a[text()='Портфель инвестора']")
    MUTUAL_SETTLEMENTS = (By.XPATH,"//a[text()='Взаиморасчеты']")
    FINANCES = (By.LINK_TEXT, "Финансы")
    TASKS = (By.CSS_SELECTOR, "li[class = 'ant-menu-item ant-menu-item-active ant-menu-item-selected']")
    REFERENCES = (By.CSS_SELECTOR, "img[src = '/assets/directories-6ea28e06.png']")
    CONTRACT_DATA = (By.LINK_TEXT, "Данные для договора")
    INVOICE_FOR_PAYMENT = (By.LINK_TEXT, "Счет для оплаты")
    INVESTORS = (By.LINK_TEXT, "Инвесторы")
    PARTNERS =(By.LINK_TEXT, "Партнеры")
    STAFF = (By.LINK_TEXT, "Сотрудники")
    SUPPLIERS = (By.LINK_TEXT, "Поставщики")
    TYPES_OF_EXPENSES = (By.LINK_TEXT, "Виды расходов")
    LENDERS = (By.LINK_TEXT, "Займодатели")
    USERS = (By.LINK_TEXT, "Пользователи")
    CLIENTS = (By.LINK_TEXT, "Клиенты")
    GARANTORS = (By.LINK_TEXT, "Поручители")
    TASKS2 = (By.XPATH,"//span[text()='Задачи']")
    MY_TASKS = (By.XPATH,"//span[text()='Мои задачи']")
    ACTIVE_TASKS = (By.XPATH,"//span[text()='Активные']")
    EXPIRED_TASKS = (By.XPATH,"//span[text()='Истекшие']")
    COMPLETED_TASKS = (By.XPATH,"//span[text()='Завершенные']")
    MENU_FOLD_BUTTON = (By.XPATH, "//button[@type='button']")
    EXIT_BUTTON = (By.XPATH,"//span[text()='Выйти']")

class StatisticsPageLocators():
    FILTERS = (By.XPATH,"//span[text()='Открыть фильтры']")





