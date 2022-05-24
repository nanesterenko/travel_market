import random
import allure
from fixtures.constants import Notice
from models.register import RegisterUserModel


class TestRegisterPage:

    @allure.feature("registration")
    @allure.story("Успешная регистрация пользователя.")
    def test_valid_registration(self, app):
        """
        1. Открыть страницу регистрации
        2. Заполнить обязательные поля валидными данными
        3. Нажать кнопку регистрации
        Ожидаемый результат: произошел редирект на страницу авторизации
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        app.register_page.register_user(data=data)
        current_url = app.register_page.get_current_url()
        assert app.login_page.URL_LOGIN_PAGE in current_url

    @allure.feature("registration")
    @allure.story("Ошибка при регистрации с различными паролями.")
    def test_registration_with_different_password(self, app):
        """
        1. Открыть страницу регистрации
        2. При заполнении полей указать различные пароли
        3. Нажать кнопку регистрации
        Ожидаемый результат: Отобразилось уведомление "The two password fields didn’t match."
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.password_1 = "different_password"
        app.register_page.register_user(data=data)
        error_msg = app.register_page.get_event_text()
        assert error_msg == Notice.ERROR_DIFFERENT_PASSWORD

    @allure.feature("registration")
    @allure.story("Ошибка при регистрации с паролями не соответствующими требованиям.")
    def test_registration_with_incorrect_password(self, app):
        """
        1. Открыть страницу регистрации
        2. При заполнении полей указать пароли не соответствующие требованиям
        3. Нажать кнопку регистрации
        Ожидаемый результат: Отобразились три уведомления
            'This password is too short. It must contain at least 8 characters.'
            'This password is too common.'
            'This password is entirely numeric.'
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.password_1 = "1"
        data.password_2 = "1"
        app.register_page.register_user(data=data)
        error_msg = app.register_page.get_event_text()
        assert Notice.ERROR_TOO_SHORT_PASSWORD in error_msg
        assert Notice.ERROR_TOO_COMMON_PASSWORD in error_msg
        assert Notice.ERROR_ONLY_NUMERIC_PASSWORD in error_msg

    @allure.feature("registration")
    @allure.story("Ошибка при повторной регистрации с такими же данными.")
    def test_repeated_registration(self, app, register_user):
        """
        Предусловие: зарегистрировать пользователя
        1. Открыть страницу регистрации
        2. Указать данные пользователя из предусловия
        3. Нажать кнопку регистрации
        Ожидаемый результат: Отобразилось уведомление "A user with that username already exists."
        """
        app.register_page.open_register_page()
        data = register_user
        app.register_page.register_user(data=data)
        error_msg = app.register_page.get_event_text()
        assert error_msg == Notice.ERROR_EXIST_USER

    @allure.feature("registration")
    @allure.story("Ошибка при регистрации с именем вместо паролями.")
    def test_registration_with_simple_password(self, app):
        """
        1. Открыть страницу регистрации
        2. При заполнении полей указать username в качестве пароля
        3. Нажать кнопку регистрации
        Ожидаемый результат: Отобразилось уведомление "The password is too similar to the username."
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.password_1 = data.user
        data.password_2 = data.user
        app.register_page.register_user(data=data)
        error_msg = app.register_page.get_event_text()
        assert Notice.ERROR_USERNAME_LIKE_PASSWORD in error_msg
        assert "test" in error_msg

    @allure.feature("registration")
    @allure.story("Ошибка при регистрации с некорректным email.")
    def test_registration_with_incorrect_email(self, app):
        """
        1. Открыть страницу регистрации
        2. Указать email с некорректным доменом
        3. Нажать кнопку регистрации
        Ожидаемый результат: Отобразилось уведомление "Enter a valid email address."
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.email = data.user + "@" + data.user
        app.register_page.register_user(data=data)
        error_msg = app.register_page.get_event_text()
        assert error_msg == Notice.ERROR_INVALID_EMAIL

    @allure.feature("registration")
    @allure.story("Ошибка при регистрации несовершеннолетнего пользователя.")
    def test_registration_with_young_age(self, app):
        """
        1. Открыть страницу регистрации
        2. Указать возраст менее 18 и нажать кнопку регистрации
        3. Проверить, что отобразилось соответствующее уведомление
        Ожидаемый результат: Отобразилось уведомление "You are young!"
        """
        app.register_page.open_register_page()
        data = RegisterUserModel.random()
        data.age = random.randint(1, 17)
        app.register_page.register_user(data=data)
        error_msg = app.register_page.get_event_text()
        assert error_msg == Notice.ERROR_INVALID_AGE

