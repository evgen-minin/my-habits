from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from my_habits.models import Habit


class HabitViewSetTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            email='evgen@minin.ru',
            first_name='Admin',
            last_name='evgen',
            is_staff=True,
            is_superuser=True,
        )
        self.user.set_password('123qwe456rty')
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        url = reverse('my_habits:my-habits-list')
        data = {
            'title': 'New Habit',
            'place': 'New place',
            'action': 'New action',
            'is_public': True,
            'user': self.user.id
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 1)
        self.assertEqual(Habit.objects.get().title, 'New Habit')

    def test_list_habits(self):
        Habit.objects.create(
            title='Habit 1',
            is_public=True,
            user=self.user
        )
        Habit.objects.create(
            title='Habit 2',
            is_public=False,
            user=self.user
        )
        url = reverse('my_habits:my-habits-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_update_habit(self):
        habit = Habit.objects.create(
            title='Old Habit',
            is_public=True,
            user=self.user
        )
        url = reverse('my_habits:my-habits-detail', args=[habit.id])
        data = {'title': 'Updated Habit'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        habit.refresh_from_db()
        self.assertEqual(habit.title, 'Updated Habit')

    def test_delete_habit(self):
        habit = Habit.objects.create(
            title='To Be Deleted',
            is_public=True,
            user=self.user
        )
        url = reverse('my_habits:my-habits-detail', args=[habit.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)
