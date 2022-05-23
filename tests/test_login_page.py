import allure
from fixtures.constants import Notice
from models.register import RegisterUserModel


class TestLoginPage:

    @allure.feature("login")
    def test_successful_login(self, app, register_user):
        """
        Предусловие: зарегистрировать нового пользователя
        1. Авторизоваться под пользователем из предусловия
        2. Проверить, что в панеле навигации отображается имя пользователя из предусловия
        """
        app.login_page.login_user(register_user.user, register_user.password_1)
        user_in_navbar = app.login_page.get_user_from_navbar()
        assert user_in_navbar == register_user.user

    @allure.feature("login")
    def test_login_with_nonexistent_user(self, app):
        """
        1. Открыть страницу авторизации
        2. Авторизоваться под незарегистрированным пользователем
        3. Проверить, что отобразилось соответствующее уведомление
        """
        app.login_page.open_login_page()
        nonexistent_user = RegisterUserModel.random()
        app.login_page.login_user(nonexistent_user.user, nonexistent_user.password_1)
        error_msg = app.login_page.get_event_text()
        assert error_msg == Notice.ERROR_NON_EXIST_USER

    @allure.feature("login")
    def test_login_with_incorrect_user(self, app, register_user):
        """
        Предусловие: зарегистрировать нового пользователя
        1. При авторизации указать логин с опечаткой
        2. Проверить, что отобразилось соответствующее уведомление
        """
        incorrect_username = register_user.user + "q"
        app.login_page.login_user(incorrect_username, register_user.password_1)
        error_msg = app.login_page.get_event_text()
        assert error_msg == Notice.ERROR_NON_EXIST_USER

    @allure.feature("login")
    def test_login_with_incorrect_password(self, app, register_user):
        """
        Предусловие: зарегистрировать нового пользователя
        1. При авторизации указать пароль с опечаткой
        2. Проверить, что отобразилось соответствующее уведомление
        """
        incorrect_password = register_user.password_1 + "1"
        app.login_page.login_user(register_user.user, incorrect_password)
        error_msg = app.login_page.get_event_text()
        assert error_msg == Notice.ERROR_NON_EXIST_USER
