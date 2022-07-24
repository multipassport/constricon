from accounts.managers import UserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from enums import League


class UserAccount(AbstractUser):
    username = None

    email = models.EmailField(
        'электронная почта',
        unique=True,
    )

    public_name = models.CharField(
        'публичное имя',
        max_length=40,
    )
    avatar = models.ImageField(
        'аватарка',
        blank=True,
    )
    league = models.CharField(
        'лига',
        choices=League.choices,
        default=League.FIRST,
        max_length=10,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
