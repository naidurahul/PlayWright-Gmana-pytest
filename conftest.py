import pytest
from playwright.sync_api import sync_playwright

# A fixture is a reusable piece of code that sets something up before a 
# test runs, and can clean it up afterward

@pytest.fixture(scope="session")
def browser():
   with sync_playwright() as p:
       browser = p.chromium.launch(headless=True)
       yield browser
       browser.close()

@pytest.fixture
def page(browser):
   page = browser.new_page()
   yield page
   page.close()

