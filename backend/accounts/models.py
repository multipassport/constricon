from accounts.managers import UserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


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

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
