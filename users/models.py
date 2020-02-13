from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = {
        (GENDER_MALE, "Male"),  # Second "Male" is the one how it displays
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    }

    LANGUAGE_ENG = "english"
    LANGUAGE_KOR = "korean"

    LANGUAGE_CHOICES = {(LANGUAGE_ENG, "Eng"), (LANGUAGE_KOR, "Kor")}

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = {(CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW")}

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True,)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=6, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
