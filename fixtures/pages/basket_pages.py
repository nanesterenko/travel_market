import logging
from selenium.webdriver.common.by import By
from fixtures.pages.base_pages import BasePage

logger = logging.getLogger("travel_market")


class BasketPage(BasePage):
    SECTION_IN_NAVBAR = (By.CLASS_NAME, 'dropdown-toggle')
    BASKET_SECTION = (By.XPATH, "//a[@href='/basket/']")  # //a[@href="/basket/"]
    HOTELS_IN_BASKET = (By.XPATH, "//div[@class='row flex-wrap form-group col-lg-sm text']")
    NAME_HOTEL_IN_BASKET = "//div[@class='row flex-wrap form-group col-lg-sm text']//span[2]"

    def open_basket(self):
        logger.info("Open basket")
        self.click(locator=self.SECTION_IN_NAVBAR)
        self.click(locator=self.BASKET_SECTION)

    def get_hotels_in_basket(self):
        hotels = self.get_all_elements(locator=self.HOTELS_IN_BASKET)
        return hotels

    @staticmethod
    def get_description_hotel_in_basket(booked_hotels: list, amount: int):
        """Получаем из корзины описание элемента по порядковому номеру."""
        description = booked_hotels[amount-1].text
        return description
