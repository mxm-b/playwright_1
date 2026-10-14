from faker import Faker


class FakeData:

    def generate_email(self):
        fake_email = Faker().email()
        return fake_email

    def generate_password(self):
        fake_password = Faker().password()
        return fake_password