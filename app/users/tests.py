import unittest

from django.test import TestCase
import pytest
from django.contrib.auth import authenticate

from .forms import RegisterUserForm


@pytest.mark.skip
class TestRegisterForms(unittest.TestCase):
    def test_form_true(self):
        form_data = {
            'username': 'user123',
            'email': 'a@a.com',
            'password1': '123456789a-!',
            'password2': '123456789a-!',
            'captcha_0': "dummy_value",
            'captcha_1': "PASSED",
            }
        form = RegisterUserForm(data=form_data)
        is_valid = form.is_valid()
        if not is_valid:
            print(form.errors)
        self.assertTrue(is_valid)

    def test_form_email(self):
        form_data = {
            'username': 'user123',
            'email': 'a@.com',
            'password1': '123456789a-!',
            'password2': '123456789a-!',
            'captcha_0': "dummy_value",
            'captcha_1': "PASSED",
            }
        form = RegisterUserForm(data=form_data)
        is_valid = form.is_valid()
        if not is_valid:
            print(form.errors)
        self.assertFalse(is_valid)

    def test_form_password_mismatch(self):
        form_data = {
            'username': 'user123',
            'email': 'a@a.com',
            'password1': '123456789-!',
            'password2': '123456789a-!',
            'captcha_0': "dummy_value",
            'captcha_1': "PASSED",
            }
        form = RegisterUserForm(data=form_data)
        is_valid = form.is_valid()
        if not is_valid:
            print(form.errors)
        self.assertFalse(is_valid)

    def test_form_short_password(self):
        form_data = {
            'username': 'user123',
            'email': 'a@a.com',
            'password1': '123-!',
            'password2': '123-!',
            'captcha_0': "dummy_value",
            'captcha_1': "PASSED",
            }
        form = RegisterUserForm(data=form_data)
        is_valid = form.is_valid()
        if not is_valid:
            print(form.errors)
        self.assertFalse(is_valid)

    def test_form_invalid_captcha(self):
        form_data = {
            'username': 'user123',
            'email': 'a@a.com',
            'password1': '123456789a-!',
            'password2': '123456789a-!',
            'captcha_0': "a",
            'captcha_1': "",
            }
        form = RegisterUserForm(data=form_data)
        is_valid = form.is_valid()
        if not is_valid:
            print(form.errors)
        self.assertFalse(is_valid)


@pytest.mark.skip
class LogInTest(TestCase):
    def setUp(self):
        form_data = {
            'username': 'user123',
            'email': 'a@a.com',
            'password1': '123456789a-!',
            'password2': '123456789a-!',
            'captcha_0': "dummy_value",
            'captcha_1': "PASSED",
        }
        form = RegisterUserForm(data=form_data)
        if form.is_valid():
            form.save()

    def test_correct(self):
        user = authenticate(username='user123', password='123456789a-!')
        self.assertTrue((user is not None) and user.is_authenticated)


if __name__ == "__main__":
    unittest.main()