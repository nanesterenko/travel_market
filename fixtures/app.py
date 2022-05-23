from fixtures.pages.accommodations_pages import AccommodationPages
from fixtures.pages.basket_pages import BasketPage
from fixtures.pages.login_pages import LoginPage
from fixtures.pages.main_pages import MainPage
from fixtures.pages.register_pages import RegisterPage


class Application:

    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.login_page = LoginPage(self)
        self.register_page = RegisterPage(self)
        self.accommodations_page = AccommodationPages(self)
        self.basket_page = BasketPage(self)
        self.main_page = MainPage(self)

    def quit(self):
        self.driver.quit()
