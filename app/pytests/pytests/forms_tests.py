import pytest
from users.forms import RegisterUserForm, LoginUserForm
from captcha.conf import settings as captcha_settings


@pytest.mark.parametrize(
    'username, email, password1, password2, captcha_0, captcha_1, validity',
    [
        ("user12", "a@a.com", "12345678a-!", "12345678a-!", "PASSED", "", False),  # captcha is not correct
        ("user1", "a@a.com", "12345678a-!", "", "PASSED", "PASSED", False),  # password2 is not correct
        ("user1", "a@a.com", "1234567899", "12345678a", "PASSED", "PASSED", False),  # password mismatch
        ("user1", "a@a.com", "12345", "12345", "PASSED", "PASSED", False),  # password is short
        ("user1", "a@.com", "12345678a-!", "12345678a-!", "PASSED", "PASSED", False),  # email is not correct
        ("user12", "a@a.com", "12345678a-!", "12345678a-!", "PASSED", "PASSED", True),  # correct
    ]
)

@pytest.mark.django_db
def test_create_account(username, email, password1, password2, captcha_0, captcha_1, validity):
    try:
        captcha_settings.CAPTCHA_TEST_MODE = True
        form = RegisterUserForm(
            data={
                "username": username,
                "email": email,
                "password1": password1,
                "password2": password2,
                "captcha_0": captcha_0,
                "captcha_1": captcha_1,
            },
        )
        if not form.is_valid():
            print(form.errors)
        assert form.is_valid() is validity
    finally:
        captcha_settings.CAPTCHA_TEST_MODE = False


@pytest.mark.parametrize(
    "username, password, validity",
    [
        ("user12", "12", False),
        ("user1", "", False),
    ],
)
@pytest.mark.django_db
def test_login(username, password, validity):
    form = LoginUserForm(
        data={
            "username": username,
            "password": password,
        },
    )
    if not form.is_valid():
        print(form.errors)
    assert form.is_valid() is validity