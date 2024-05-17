from .base_page import BasePage
from .locators import MainPageLocators
import time

class MainPage(BasePage):
    def go_to_statistics(self):
        statistics = self.browser.find_element(*MainPageLocators.STATISTICS)
        statistics.click()

    def go_to_deal(self):
        deal = self.browser.find_element(*MainPageLocators.DEAL)
        deal.click()

    def go_to_chat(self):
        chat = self.browser.find_element(*MainPageLocators.CHAT)
        chat.click()

    def go_to_reports_profits(self):
        reports = self.browser.find_element(*MainPageLocators.REPORTS)
        reports.click()
        profits = self.browser.find_element(*MainPageLocators.PROFITS)
        profits.click()

    def go_to_reports_investors_portfolio(self):
        reports = self.browser.find_element(*MainPageLocators.REPORTS)
        reports.click()
        investors_portfolio = self.browser.find_element(*MainPageLocators.INVESTORS_PORTFOLIO)
        investors_portfolio.click()

    def go_to_reports_mutual_settlements(self):
        reports = self.browser.find_element(*MainPageLocators.REPORTS)
        reports.click()
        mutual_settlements = self.browser.find_element(*MainPageLocators.MUTUAL_SETTLEMENTS)
        mutual_settlements.click()

    def go_to_finances(self):
        finances = self.browser.find_element(*MainPageLocators.FINANCES)
        finances.click()

    def go_to_tasks(self):
        tasks = self.browser.find_element(*MainPageLocators.TASKS)
        tasks.click()

    def go_to_references_contract_data(self):
        references = self.browser.find_element(*MainPageLocators.REFERENCES)
        references.click()
        contract_data = self.browser.find_element(*MainPageLocators.CONTRACT_DATA)
        contract_data.click()

    def go_to_references_invoice_for_payment(self):
        references = self.browser.find_element(*MainPageLocators.REFERENCES)
        references.click()
        invoice_for_payment = self.browser.find_element(*MainPageLocators.INVOICE_FOR_PAYMENT)
        invoice_for_payment.click()

    def go_to_references_investors(self):
        references = self.browser.find_element(*MainPageLocators.REFERENCES)
        references.click()
        investors = self.browser.find_element(*MainPageLocators.INVESTORS)
        investors.click()

    def go_to_references_partners(self):
        references = self.browser.find_element(*MainPageLocators.REFERENCES)
        references.click()
        partners = self.browser.find_element(*MainPageLocators.PARTNERS)
        partners.click()

    def go_to_references_staff(self):
        references = self.browser.find_element(*MainPageLocators.REFERENCES)
        references.click()
        staff = self.browser.find_element(*MainPageLocators.STAFF)
        staff.click()

    def go_to_references_suppliers(self):
        references = self.browser.find_element(*MainPageLocators.REFERENCES)
        references.click()
        suppliers = self.browser.find_element(*MainPageLocators.SUPPLIERS)
        suppliers.click()

    def go_to_references_types_of_expenses(self):
        references = self.browser.find_element(*MainPageLocators.REFERENCES)
        references.click()
        types_of_expenses = self.browser.find_element(*MainPageLocators.TYPES_OF_EXPENSES)
        types_of_expenses.click()

    def go_to_references_lenders(self):
        references = self.browser.find_element(*MainPageLocators.REFERENCES)
        references.click()
        lenders = self.browser.find_element(*MainPageLocators.LENDERS)
        lenders.click()

    def go_to_references_users(self):
        references = self.browser.find_element(*MainPageLocators.REFERENCES)
        references.click()
        users = self.browser.find_element(*MainPageLocators.USERS)
        users.click()

    def go_to_references_clients(self):
        references = self.browser.find_element(*MainPageLocators.REFERENCES)
        references.click()
        clients = self.browser.find_element(*MainPageLocators.CLIENTS)
        clients.click()

    def go_to_references_garantors(self):
        references = self.browser.find_element(*MainPageLocators.REFERENCES)
        references.click()
        garantors = self.browser.find_element(*MainPageLocators.GARANTORS)
        garantors.click()

    def go_to_tasks2(self):
        tasks2 = self.browser.find_element(*MainPageLocators.TASKS2)
        tasks2.click()

    def go_to_my_tasks(self):
        my_tasks = self.browser.find_element(*MainPageLocators.MY_TASKS)
        my_tasks.click()

    def go_to_active_tasks(self):
        active_tasks = self.browser.find_element(*MainPageLocators.ACTIVE_TASKS)
        active_tasks.click()

    def go_to_expired_tasks(self):
        expired_tasks = self.browser.find_element(*MainPageLocators.EXPIRED_TASKS)
        expired_tasks.click()

    def go_to_completed_tasks(self):
        completed_tasks = self.browser.find_element(*MainPageLocators.COMPLETED_TASKS)
        completed_tasks.click()

    def go_to_menu_fold(self):
        menu_fold = self.browser.find_element(*MainPageLocators.MENU_FOLD_BUTTON)
        menu_fold.click()
        menu_fold.click()

    def go_to_login_page(self):
        exit_button = self.browser.find_element(*MainPageLocators.EXIT_BUTTON)
        exit_button.click()

