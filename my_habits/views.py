from django.db.models import Q
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from my_habits.models import Habit
from my_habits.paginators import HabitsPagination
from my_habits.serializers.habit import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    """
    API endpoint для привычек пользователя.

    Предоставляет операции CRUD (создание, чтение, обновление, удаление) для привычек.

    Параметры:
    - serializer_class: Сериализатор для привычек.
    - queryset: Запрос для получения всех привычек.
    - authentication_classes: Список классов аутентификации.
    - permission_classes: Список классов разрешений.

    Метод get_queryset переопределен для возвращения привычек текущего пользователя
    или публичных привычек, если пользователь аутентифицирован.
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    authentication_classes = [SessionAuthentication, TokenAuthentication, JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = HabitsPagination

    def get_queryset(self):
        user = self.request.user  # Получаем текущего пользователя
        # Возвращаем привычки текущего пользователя или публичные
        return Habit.objects.filter(Q(user=user) | Q(is_public=True))
