import logging
import random

from selenium.webdriver.common.by import By
from fixtures.pages.base_pages import BasePage

logger = logging.getLogger("travel_market")


class AccommodationPages(BasePage):
    MORE_BUTTON = (By.CLASS_NAME, 'btn-danger')
    ACCOMMODATION_SECTION = (By.XPATH, "//a[@href='/list_of_accommodations/']")
    BOOK_BUTTON = (By.CLASS_NAME, 'float-right')
    NAME_HOTEL_ON_PAGE = (By.XPATH, "//h1[@class='mt-3 ml-3']")

    def open_accommodations_page(self):
        logger.info("Open hotels page")
        self.open_site(self.app.url)
        self.click(locator=self.ACCOMMODATION_SECTION)

    def get_more_buttons(self):
        buttons = self.get_all_elements(locator=self.MORE_BUTTON)
        return buttons

    def select_random_hotel(self, listing: list, count: int):
        logger.info("Chose a random hotel for booking")
        number = random.randint(1, count)
        self.click_from_list(listing, number)

    def book_hotel(self):
        self.click(locator=self.BOOK_BUTTON)

    def get_name_selected_hotel(self):
        name = self.text(locator=self.NAME_HOTEL_ON_PAGE)
        return name
