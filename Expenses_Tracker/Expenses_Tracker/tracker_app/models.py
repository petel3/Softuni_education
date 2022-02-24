from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from Expenses_Tracker.tracker_app.validators import only_letters_validator, MaxFileSizeValidator


class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 15

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0

    IMAGE_MAX_SIZE_IN_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            only_letters_validator,
        )
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            only_letters_validator,
        )
    )
    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        ),
    )
    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        blank=True,
        null=True,
        validators=(
            MaxFileSizeValidator(IMAGE_MAX_SIZE_IN_MB),
        )

    )
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Expense(models.Model):
    TITLE_MAX_LEN = 30
    title = models.CharField(
        max_length=TITLE_MAX_LEN
    )
    expense_image = models.URLField()
    description = models.TextField(
        blank=True,
        null=True,
    )
    price = models.FloatField()
