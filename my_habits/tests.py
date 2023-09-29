from datetime import datetime

from django.core import mail
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status

from my_habits.models import Habit
from my_habits.tasks import send_habit_notification
from users.models import User

from rest_framework.test import APITestCase


class SendHabitNotificationTestCase(TestCase):

    def test_send_habit_notification(self):
        # Создаём  пользователя и привычку
        user = User.objects.create(email='evgen@minin.ru', password='123qwe456rty')
        habit = Habit.objects.create(
            user=user,
            title='Test Habit',
            time=timezone.now().time(),  # Устанавливаем текущее время
            time_required=60,  # Устанавливаем время выполнения
            is_reward=True,
        )

        # Вызываем задачу
        send_habit_notification(habit.id)

        # Проверьте, было ли отправлено уведомление
        self.assertEqual(len(mail.outbox), 1)  # Проверка, что было отправлено одно уведомление
        self.assertEqual(mail.outbox[0].subject, 'Уведомление')  # Проверка темы уведомления
        self.assertIn('Test Habit', mail.outbox[0].body)  # Проверка содержания уведомления


class HabitAPITestCase(APITestCase):
    def setUp(self):
        # Создаем пользователя
        self.user = User.objects.create_user(email='evgen@minin.ru', password='123qwe456rty')
        self.client.login(username='testuser', password='testpassword')

    def test_create_habit(self):
        url = reverse('habit-list')
        data = {
            'user': self.user.id,
            'title': 'Test Habit',
            'place': 'Test Place',
            'time': '08:00:00',
            'action': 'Test Action',
            'frequency': 7,
            'time_required': 3600  # 1 час в секундах
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 1)
