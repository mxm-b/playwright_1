from faker import Faker


class FakeData:

    def __init__(self):
        self.fake = Faker()

    def generate_email(self):
        fake_email = self.fake.email()
        return fake_email

    def generate_password(self):
        fake_password = self.fake.password()
        return fake_password