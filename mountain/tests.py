from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase


class UserLoginTestCase(TestCase):
    ...

    # some setup here, explained later

    def test_correct_login(self):
        # unit test
        # Corroborate the expected scenario
        ...

    def test_if_password_incorrect_then_cant_login(self):
        # unit test
        # Corroborate that user's password needs to be only the correct one
        ...

    def test_if_user_not_registered_cant_login(self):
        pass


class LoginTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
