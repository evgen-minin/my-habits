from celery import shared_task
from django.utils import timezone

from my_habits.models import Habit


@shared_task
def send_habit_notification(habit_id):
    habit = Habit.objects.get(pk=habit_id)
    user = habit.user

    # Проверяем, нужно ли отправлять уведомление для привычки
    if habit.time and habit.time_required:
        current_time = timezone.now().time()
        if current_time >= habit.time:
            user.email_user('Уведомление', 'Выполните свою привычку: ' + habit.title)
