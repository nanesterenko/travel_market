import random
from faker import Faker

fake = Faker()


class RegisterUserModel:
    """Генерация фейковых данных для успешной регистрации."""

    def __init__(self, user: str = None, email: str = None, password_1: str = None, password_2: str = None,
                 domain: str = None, age: int = None):
        self.user = user
        self.email = email
        self.password_1 = password_1
        self.password_2 = password_2
        self.domain = domain
        self.age = age

    @staticmethod
    def random():
        user = f"{random.randint(10, 1000)}_{fake.first_name()}"
        email = f"{random.randint(100, 1000)}_{fake.email()}"
        password = fake.password()
        domain = fake.domain_name()
        age = fake.pyint(18, 99)
        return RegisterUserModel(user=user, email=email, password_1=password, password_2=password,
                                 domain=domain, age=age)
