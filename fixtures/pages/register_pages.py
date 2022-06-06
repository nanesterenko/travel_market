import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_pages import BasePage
from models.register import RegisterUserModel

logger = logging.getLogger("travel_market")


class RegisterPage(BasePage):
    LOGIN_SECTION = (By.XPATH, "//a[@href='/auth/login/']")
    REGISTER_SECTION = (By.XPATH, "//a[@href='/auth/register/']")
    USERNAME_INPUT = (By.ID, 'id_username')
    FIRST_NAME_INPUT = (By.ID, 'id_first_name')
    PASSWORD_INPUT = (By.ID, 'id_password1')
    PASSWORD_REPEAT_INPUT = (By.ID, 'id_password2')
    EMAIL_INPUT = (By.ID, 'id_email')
    AGE_INPUT = (By.ID, 'id_age')
    REGISTER_BUTTON = (By.XPATH, "//input[@value='register']")
    ERROR_MSG = (By.CLASS_NAME, 'errorlist')
    AVATAR = (By.ID, "id_avatar")

    def open_register_page(self):
        self.open_site(self.app.url)
        self.click(locator=self.LOGIN_SECTION)
        self.click(locator=self.REGISTER_SECTION)

    def register_user(self, data: RegisterUserModel, path: str = None):
        logger.info(f"Registered user with email {data.user} - {data.password_1}")
        self.fill(locator=self.USERNAME_INPUT, value=data.user)
        self.fill(locator=self.FIRST_NAME_INPUT, value=data.user)
        self.fill(locator=self.EMAIL_INPUT, value=data.email)
        if path is not None:
            self.upload_image(locator=self.AVATAR, path_to_file=path)
        self.clear(locator=self.AGE_INPUT)
        self.fill(locator=self.AGE_INPUT, value=data.age)
        self.fill(locator=self.PASSWORD_INPUT, value=data.password_1)
        self.fill(locator=self.PASSWORD_REPEAT_INPUT, value=data.password_2)
        self.click(locator=self.REGISTER_BUTTON)

    def get_event_text(self) -> str:
        message = self.text(locator=self.ERROR_MSG)
        return message
