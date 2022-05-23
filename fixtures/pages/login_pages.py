import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_pages import BasePage

logger = logging.getLogger("travel_market")


class LoginPage(BasePage):
    LOGIN_SECTION = (By.XPATH, "//a[@href='/auth/login/']")
    USERNAME_INPUT = (By.XPATH, "//input[@id='id_username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='id_password']")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='log in']")
    USER_PROFILE_IN_NAVBAR = (By.XPATH, "//a[@data-toggle='dropdown']")
    ERROR_MSG = (By.CLASS_NAME, 'errorlist')
    URL_LOGIN_PAGE = "/auth/login/"

    def open_login_page(self):
        self.open_site(self.app.url)
        self.click(locator=self.LOGIN_SECTION)

    def login_user(self, username: str, password: str):
        logger.info(f"Login user with username={username}")
        self.fill(locator=self.USERNAME_INPUT, value=username)
        self.fill(locator=self.PASSWORD_INPUT, value=password)
        self.click(locator=self.LOGIN_BUTTON)

    def get_user_from_navbar(self):
        return self.text(locator=self.USER_PROFILE_IN_NAVBAR)

    def get_event_text(self):
        message = self.text(locator=self.ERROR_MSG)
        return message

