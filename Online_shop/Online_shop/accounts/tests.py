from datetime import date

from django.test import TestCase

from Online_shop.accounts.models import ShopUser, Profile


class URLTests(TestCase):
    def test_loginpage(self):
        response=self.client.get('/accounts/login/')
        self.assertEqual(response.status_code,200)

    def test_registerpage(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)

    def test_logoutpage(self):
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.get('').status_code, 200)

class AccountAndUserTests(TestCase):
    VALID_USER_CREDENTIALS={
        'username': 'django1',
        'password': 'Valkyrie123',
    }
    VALID_PROFILE_DATA={

            'first_name': 'Test',
            'last_name': 'User',
            'picture': 'http://test.picture/url.png',
            'description': "Some text",
            'email': "petel.popov@gmail.com",
            'gender': "Male"
    }

    def __create_user(self, **credentials):
        return ShopUser.objects.create_user(**credentials)

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        return (user, profile)