from django.contrib import admin
from django.db.models import Q

from my_habits.models import Habit


class HabitAdmin(admin.ModelAdmin):
    """
    Класс административной настройки модели Habit.

    Определяет отображаемые поля и фильтрацию списка привычек
    в зависимости от прав пользователя.

    Поля:
    - title (str): Заголовок привычки.
    - user (str): Пользователь, создавший привычку.
    - is_public (bool): Признак публичной привычки.
    """
    list_display = ('title', 'user', 'is_public')

    def get_queryset(self, request):
        """
         Получает список привычек в зависимости от прав пользователя.

        Если пользователь является суперпользователем, возвращает все привычки.
        В противном случае, возвращает только привычки текущего пользователя
        или публичные привычки.
        """
        if request.user.is_superuser:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(Q(user=request.user) | Q(is_public=True))


admin.site.register(Habit, HabitAdmin)
