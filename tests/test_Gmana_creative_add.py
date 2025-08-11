import re
from playwright.sync_api import Page, expect
from pages.Gmana_login_page import LoginPage


def test_example(page: Page) -> None:
    login_page = LoginPage(page)
    page.goto("https://stg1.g-mana.live/app/login")
    login_page.enter_email("rahul.naidu.stg1@g-mana.com")
    login_page.enter_password("hX9^4wxmZUpgRMzL")
    login_page.click_login()
    
    page.get_by_role("link", name=" Slates").click()
    page.get_by_role("button", name="").click()
    page.get_by_role("menuitem", name=" My Profile").click()
    page.get_by_role("textbox", name="Job title").click()
    page.get_by_role("textbox", name="Job title").clear()
    page.get_by_role("textbox", name="Job title").fill("Quality check officer")
    # page.screenshot(path="ex.png")
    page.get_by_role("button", name="OK").click()
    page.get_by_role("button", name="").click()
    page.get_by_role("menuitem", name=" Logout").click()
