from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Расширенная модель пользователя (User) с использованием электронной почты вместо имени пользователя.

    Поля:
    - email: Электронная почта пользователя (уникальное поле).
    - avatar: Изображение-аватар пользователя (загружается в папку 'users/', может быть пустым).
    - phone_number: Номер телефона пользователя (максимум 20 символов, может быть пустым).


    Поля, унаследованные от AbstractUser:
    - username: Имя пользователя (не используется, заменено на email).
    - password: Пароль пользователя.
    - first_name: Имя пользователя.
    - last_name: Фамилия пользователя.
    - date_joined: Дата и время регистрации пользователя.
    - is_active: Флаг активности пользователя.
    - is_staff: Флаг присвоения пользователю статуса персонала.
    - is_superuser: Флаг суперпользователя.
    - groups: Группы, к которым принадлежит пользователь.
    - user_permissions: Права доступа пользователя.

    Управление аутентификацией:
    - USERNAME_FIELD: Поле, используемое для аутентификации (email).
    - REQUIRED_FIELDS: Список обязательных полей при создании пользователя (по умолчанию пуст).

    """
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='аватар', blank=True, null=True)
    phone_number = models.CharField(max_length=35, verbose_name='телефон', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
