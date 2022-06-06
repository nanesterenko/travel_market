import allure
from fixtures.constants import Notice
from models.register import RegisterUserModel


class TestLoginPage:

    @allure.feature("login")
    @allure.story("Успешная авторизация.")
    def test_successful_login(self, app, register_user):
        """
        Предусловие: зарегистрировать нового пользователя
        1. Открыть страницу авторизации
        2. Указать корректные данные в полях username и password
        3. Нажать кнопку авторизации
        Ожидаемый результат: в панели навигации отображается имя пользователя
        """
        app.login_page.login_user(register_user.user, register_user.password_1)
        user_in_navbar = app.login_page.get_user_from_navbar()
        assert user_in_navbar == register_user.user

    @allure.feature("login")
    @allure.story("Ошибка при авторизации несуществующего пользователя.")
    def test_login_with_nonexistent_user(self, app):
        """
        1. Открыть страницу авторизации
        2. В полях username и password указать данные несуществующего пользователя
        3. Нажать кнопку авторизации
        Ожидаемый результат: Отображается уведомление "Please enter a correct username and password.
         Note that both fields may be case-sensitive."
        """
        app.login_page.open_login_page()
        nonexistent_user = RegisterUserModel.random()
        app.login_page.login_user(nonexistent_user.user, nonexistent_user.password_1)
        error_msg = app.login_page.get_event_text()
        assert error_msg == Notice.ERROR_NON_EXIST_USER

    @allure.feature("login")
    @allure.story("Ошибка при авторизации с пустым полем Username.")
    def test_login_with_nonexistent_user(self, app):
        """
        1. Открыть страницу авторизации
        2. Заполнить поля, кроме Username
        3. Нажать кнопку авторизации
        Ожидаемый результат: Отображается уведомление ""
        """
        app.login_page.open_login_page()
        user = RegisterUserModel.random()
        app.login_page.login_user(None, user.password_1)
        error_msg = app.login_page.get_event_text()
        assert error_msg == Notice.ERROR_NON_EXIST_USER

    @allure.feature("login")
    @allure.story("Ошибка при авторизации с некорректным логином.")
    def test_login_with_incorrect_user(self, app, register_user):
        """
        Предусловие: зарегистрировать нового пользователя
        1. Открыть страницу авторизации
        2. Указать логин с опечаткой и корректный пароль
        3. Нажать кнопку авторизации
        Ожидаемый результат: Отображается уведомление "Please enter a correct username and password.
         Note that both fields may be case-sensitive."
        """
        incorrect_username = register_user.user + "q"
        app.login_page.login_user(incorrect_username, register_user.password_1)
        error_msg = app.login_page.get_event_text()
        assert error_msg == Notice.ERROR_NON_EXIST_USER

    @allure.feature("login")
    @allure.story("Ошибка при авторизации с некорректным паролем.")
    def test_login_with_incorrect_password(self, app, register_user):
        """
        Предусловие: зарегистрировать нового пользователя
        1. Открыть страницу авторизации
        2. Указать корректный логин и пароль с опечаткой
        3. Нажать кнопку авторизации
        Ожидаемый результат: Отображается уведомление "Please enter a correct username and password.
         Note that both fields may be case-sensitive."
        """
        incorrect_password = register_user.password_1 + "1"
        app.login_page.login_user(register_user.user, incorrect_password)
        error_msg = app.login_page.get_event_text()
        assert error_msg == Notice.ERROR_NON_EXIST_USER
