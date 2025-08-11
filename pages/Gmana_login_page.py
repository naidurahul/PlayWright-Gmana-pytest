from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page:Page):
        self.page = Page
        self.Email_input = page.get_by_role("textbox", name = "Email")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def enter_email(self, email:str):
        self.Email_input.fill(email)

    def enter_password(self, password:str):
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

        
            