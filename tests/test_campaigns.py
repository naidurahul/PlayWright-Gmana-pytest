import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://stg1.g-mana.live/app/login")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("<-add email->")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("<-add password->")
    page.get_by_role("button", name="Login").click()
    page.get_by_text("Demand").click()
    page.get_by_role("link", name="Campaigns").click()
    page.locator("(//*[name()='svg'][@role='button'])[1]").click()
    page.wait_for_timeout(1000)  # Wait for filter modal to be fully visible
    search_input = page.get_by_role("textbox", name="Search Campaign")
    search_input.click()
    
    # Type each character slowly to match human typing and allow for updates
    for char in "rahul":
        search_input.type(char, delay=100)  # Add delay between keystrokes
        page.wait_for_timeout(300)  # Give time for the search to update after each character
        
    # Final wait to ensure the last character's search completes
    page.wait_for_timeout(1000)
    # page.wait_for_selector('text="Rahul Campaign dont touch for testing"', timeout=5000)
    page.locator("#filter-modal___BV_modal_header_ i").click()
    page.locator("(//i[@title='Edit Campaign'])[2]").click()
    # page.get_by_role("row", name="Rahul Campaign dont touch for").get_by_role("button").nth(1).click()
    # Click the End Date input using the label
    page.locator('label[for="scheduleEndDate"] + input').click()
    next_btn = page.get_by_role("cell", name=" Next Month").locator("i")

    for _ in range(3):
        next_btn.click(delay=1000)

    page.get_by_role("cell", name="April 2032 Toggle Date and Time").click()
    page.get_by_text("Mar", exact=True).click()
    page.get_by_role("cell", name="11").click()
    page.get_by_title("Close the picker").click()
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="").click()
    page.get_by_role("menuitem", name=" Logout").click()
