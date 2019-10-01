from django.contrib.auth.models import AbstractUser
from django.db                  import models

class User(AbstractUser):

    Gender_Male = "male"
    Gender_Female = "female"
    Gender_Others = "other"

    Gender_Choices = (
        (Gender_Male, "Male"),
        (Gender_Female, "Female"),
        (Gender_Others, "Others"),
    )

    Language_KOREAN   = "KR"
    Language_English  = "EN"
    Language_Chinese  = "CN"
    Language_Japanese = "JP"

    Language_Choices = (
        (Language_KOREAN, "Korean"),
        (Language_English, "English"),
        (Language_Chinese, "Chinese"),
        (Language_Japanese, "Japanese")
    )

    Currency_KRW = "KRW"
    Currency_USD = "USD"
    Currency_EUR = "EUR"

    Currency_Choices = (
        (Currency_KRW, "KRW"),
        (Currency_USD, "USD"),
        (Currency_EUR, "EUR")
    )

    bio       = models.TextField(default="")
    birthday  = models.DateField(blank=True, null= True)
    gender    = models.CharField(choices=Gender_Choices, max_length=10, blank=True)
    avatar    = models.ImageField(blank=True)
    language  = models.CharField(choices=Language_Choices, max_length=2, blank=True,
    default   = "Korean")
    currency  = models.CharField(choices=Currency_Choices, max_length=3, blank=True,
    default   = "KRW")
    superhost = models.BooleanField(default=False)

