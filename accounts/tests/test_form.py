from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse

from accounts.forms import RegistrationForm, LoginForm
from accounts.models import Account


class TestAccountForm(TestCase):

    def setUp(self):
        self.user = RegistrationForm(data={
            "email": "wbrebin@gmail.com",
            "username": "Gamer",
            "password1": "game is live12",
            "password2": "game is live12",
        })

    # create user with sending data to all fields test
    def test_create_user_with_true_all_fields(self):
        """
        it should return 'True' for form.is_valid() method everytime; because all fields has filled with
        valid data
        """

        user = RegistrationForm(data={
            "email": "gamerland1029@gmail.com",
            "username": "Gamer",
            "password1": "game is live12",
            "password2": "game is live12",
        })
        self.assertTrue(user.is_valid())
        self.assertEquals(len(user.errors), 0)

    # create user with sending invalid email for email field test
    def test_create_user_with_false_email(self):
        """
        this test should return 'False' for form.is_valid() method everytime.
        """

        user = RegistrationForm(data={
            "email": "gamerland1029",
            "username": "Gamer",
            "password1": "game is live12",
            "password2": "game is live12",
        })
        self.assertFalse(user.is_valid())
        self.assertEquals(len(user.errors), 1)

    # create user with sending invalid password for password field test
    def test_create_user_with_false_password_confirmation(self):
        """
        this test should return 'False' for form.is_valid() method everytime; because for create valid user,
        we must send as same as password for both password fields ('password1', 'password2').
        """

        user = RegistrationForm(data={
            "email": "gamerland1029@gmail.com",
            "username": "Gamer",
            "password1": "game is live",
            "password2": "game is live12",
        })
        self.assertFalse(user.is_valid())
        self.assertEquals(len(user.errors), 1)

    # create user with email that exists before test
    def test_create_user_with_exists_user_email(self):
        """
        this test should return 'False' for form.is_valid() method everytime; because create user with exists email
        is not allowed.
        """

        user = RegistrationForm(data={
            "email": self.user["email"],
            "username": "Gamer1",
            "password1": "game is live12",
            "password2": "game is live12",
        })
        self.assertFalse(user.is_valid())
        self.assertEquals(len(user.errors), 1)

    # create user without sending data for username field test
    def test_create_user_with_null_username_field(self):
        """
        this test should return 'False' for form.is_valid() method everytime; because create user without username
        is not allowed.
        """

        user = RegistrationForm(data={
            "email": "gamerland1029@gmail.com",
            "username": "",
            "password1": "game is live12",
            "password2": "game is live12",
        })
        self.assertFalse(user.is_valid())
        self.assertEquals(len(user.errors), 1)

    # create user without email test
    def test_create_user_with_null_email_field(self):
        """
        this test should return 'False' for form.is_valid() method everytime; because create user without email
        is not allowed.
        """

        user = RegistrationForm(data={
            "email": "",
            "username": "Gamer",
            "password1": "game is live12",
            "password2": "game is live12",
        })
        self.assertFalse(user.is_valid())
        self.assertEquals(len(user.errors), 1)

    # create user without password1 test
    def test_create_user_with_null_password_field(self):
        """
        this test should return 'False' for form.is_valid() method everytime; because for create new use, we must
        use password and if we don't send any values for each password fields.
        """

        user = RegistrationForm(data={
            "email": "gamerland1029@gmail.com",
            "username": "Gamer",
            "password1": "",
            "password2": "game is live12",
        })
        self.assertFalse(user.is_valid())
        self.assertEquals(len(user.errors), 1)

    # create user without send any data for both fields of password (both fields is null) test
    def test_create_user_with_null_both_password_fields(self):
        """
        this test should return 'False' everytime for form.is_valid() method; because create user without
        password isn't allowed.
        """

        user = RegistrationForm(data={
            "email": "gamerland1029@gmail.com",
            "username": "Gamer",
            "password1": "",
            "password2": "",
        })
        self.assertFalse(user.is_valid())
        self.assertEquals(len(user.errors), 2)

    # create user without sending any values for any fields test
    def test_create_user_with_null_all_fields(self):
        """
        this test should return 'False' everytime for form.is_valid() method; because create user without
        any information isn't allowed.
        """

        user = RegistrationForm(data={
            "email": "",
            "username": "",
            "password1": "",
            "password2": "",
        })
        self.assertFalse(user.is_valid())
        self.assertEquals(len(user.errors), 4)


# Login Form Test
class TestLoginForm(TestCase):

    @classmethod
    def setUpTestData(cls):
       cls.user = Account.objects.create_user(email="wbrebin@gmail.com", username="rebin", password="123456789WB")


    # Login with Valid Fields test
    def test_login_with_valid_information(self):
        """
        this test should return True for form.is_valid() Everytime
        """
        response = LoginForm(data={
            "email": "wbrebin@gmail.com",
            "password": "123456789WB"
        })

        self.assertEquals(response.is_valid(), True)
        self.assertEquals(len(response.errors), 0)


    # Login with Invalid Email Field test
    def test_login_with_invalid_email(self):
        """
        this test should return False for form.is_valid() Everytime. Because Email is Invalid
        """
        response = LoginForm(data={
            "email": "wbrebin123@gmail.com",
            "password": "123456789WB"
        })

        self.assertFalse(response.is_valid())
        self.assertEquals(len(response.errors), 1)


    # Login with Invalid Password Field test
    def test_login_with_invalid_password(self):
        """
        this test should return False for form.is_valid() Everytime. Because Password is Invalid
        """
        response = LoginForm(data={
            "email": "wbrebin@gmail.com",
            "password": "12345WB"
        })

        self.assertFalse(response.is_valid())
        self.assertEquals(len(response.errors), 1)


    # Login with Empty Fields test
    def test_login_with_empty_fields(self):
        """
        this test should return False for form.is_valid() Everytime. Because Password and Email Fields are Empty
        """
        response = LoginForm(data={
            "email": "",
            "password": ""
        })

        self.assertFalse(response.is_valid())
        self.assertEquals(len(response.errors), 2)

