from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import time

class TestLinksOnMainPage():
    def test_pages_on_main_page(self, browser):
        link = "http://45.12.236.43/login"
        page = LoginPage(browser, link)
        page.open()
        browser.refresh()
        page.authentication()
        page = MainPage(browser, link)
        page.go_to_statistics()
        page.go_to_deal()
        page.go_to_chat()
        page.go_to_reports_profits()
        page.go_to_reports_investors_portfolio()
        page.go_to_reports_mutual_settlements()
        page.go_to_finances()
        page.go_to_tasks()
        page.go_to_references_contract_data()
        page.go_to_references_invoice_for_payment()
        page.go_to_references_investors()
        page.go_to_references_partners()
        page.go_to_references_staff()
        page.go_to_references_suppliers()
        page.go_to_references_types_of_expenses()
        page.go_to_references_lenders()
        page.go_to_references_users()
        page.go_to_references_clients()
        page.go_to_references_garantors()
        page.go_to_tasks2()
        page.go_to_my_tasks()
        page.go_to_active_tasks()
        page.go_to_expired_tasks()
        page.go_to_completed_tasks()
        page.go_to_menu_fold()
        page.go_to_login_page()
        time.sleep(1)
