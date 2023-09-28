from rest_framework import serializers

from my_habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """
     Сериализатор для модели привычки.

    Параметры:
    - model: Модель, которую сериализатор будет представлять.
    - fields: Перечень полей модели, которые будут сериализованы.

    Этот сериализатор используется для преобразования объектов модели привычки в JSON-представление.
    """
    class Meta:
        model = Habit
        fields = (
            'title',
            'place',
            'action',
        )
