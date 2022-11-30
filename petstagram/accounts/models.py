from enum import Enum

from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models

from petstagram.core.validators import validate_only_letters


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'
    DoNotShow = 'Do not show'


class AppUser(auth_models.AbstractUser):
    MIN_LENGTH_FIRST_NAME = 2
    MAX_LENGTH_FIRST_NAME = 30
    MIN_LENGTH_LAST_NAME = 2
    MAX_LENGTH_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(
            validate_only_letters,
            validators.MinLengthValidator(MIN_LENGTH_FIRST_NAME),
        )
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(
            validate_only_letters,
            validators.MinLengthValidator(MIN_LENGTH_LAST_NAME),
        )
    )
    email = models.EmailField(
        unique=True,
    )
    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
    )

    # Users log in with email
    # USERNAME_FIELD = 'email'
