import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_pages import BasePage

logger = logging.getLogger("travel_market")


class MainPage(BasePage):
    MAIN_LOGO = (By.CLASS_NAME, "navbar-brand")
    CAROUSEL_ITEMS = (By.XPATH, "//img[@class='d-block w-100']/@src")
    BUTTON_ACCOMMODATIONS = (By.XPATH, "//div[@class='card-body']/a[@href='/list_of_accommodations/']")
    SEARCH_INPUT = (By.XPATH, "/input[@type='search']")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    def open_main_page(self):
        self.open_site(self.app.url)

    def get_count_items(self):
        p = self.get_all_elements(locator=self.CAROUSEL_ITEMS)
        return p
