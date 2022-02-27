import re

from django.core.exceptions import ValidationError


def only_letters_numbers_and_underscores_validator(value):
    if not re.match("^[A-Za-z0-9_-]*$", value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
