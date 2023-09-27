from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """
    Создаёт суперпользователя с определенными данными, используя эту команду.

    Использование:
    python manage.py create_superuser
    """

    def handle(self, *args, **options):
        """
        Обработчик команды get_or_create.

        Создаёт суперпользователя с указанными данными.

        """
        user, created = User.objects.get_or_create(
            email='evgen@minin.ru',
            defaults={
                'first_name': 'Admin',
                'last_name': 'evgen',
                'is_staff': True,
                'is_superuser': True,
            }
        )

        if created:
            user.set_password('123qwe456rty')
            user.save()
            self.stdout.write(self.style.SUCCESS("Суперпользователь успешно создан."))
        else:
            self.stdout.write(self.style.SUCCESS("Суперпользователь уже существует."))
