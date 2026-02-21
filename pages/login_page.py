class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_field = page.get_by_placeholder("Username")
        self.password_field = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def load(self, url):
        self.page.goto(url)

    def login(self, user, pwd):
        self.username_field.fill(user)
        self.password_field.fill(pwd)
        self.login_button.click()