from rest_framework import serializers

from my_habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            'title',
            'place',
            'action',
        )
