from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from my_habits.models import Habit
from my_habits.serializers.habit import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
