import allure


class TestBookingPage:

    @allure.feature("booking")
    @allure.story("Успешное бронирование отеля.")
    def test_successful_booking(self, app, login_user):
        """
        Предусловия: зарегистрировать и авторизоваться под новым пользователем
        1. Открыть страницу со списком отелей
        2. Проверить что на странице доступны отели для бронирования
        3. Перейти к описанию случайного отеля
        4. Забронировать выбранный отель
        5. Открыть корзину
        Ожидаемый результат: в корзине доступен один отель и его название соответствует выбранному на шаге 3
        """
        app.accommodations_page.open_accommodations_page()
        more_about_hotel = app.accommodations_page.get_more_buttons()
        amount_hotels = len(more_about_hotel)
        assert amount_hotels > 0
        app.accommodations_page.select_random_hotel(more_about_hotel, amount_hotels)
        name_hotel_from_page = app.accommodations_page.get_name_selected_hotel()
        app.accommodations_page.book_hotel()
        app.basket_page.open_basket()
        booked_hotels = app.basket_page.get_hotels_in_basket()
        amount_hotels_in_basket = len(booked_hotels)
        assert amount_hotels_in_basket == 1
        description_hotel_in_basket = app.basket_page.\
            get_description_hotel_in_basket(booked_hotels, amount_hotels_in_basket)
        assert name_hotel_from_page in description_hotel_in_basket
