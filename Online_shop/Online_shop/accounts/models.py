from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models

from Online_shop.accounts.managers import ShopUserManager


class ShopUser(auth_models.AbstractUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LEN = 25
    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'
    objects = ShopUserManager()


class Profile(models.Model):
    
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),

        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),

        )
    )

    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
        default=DO_NOT_SHOW,
    )
