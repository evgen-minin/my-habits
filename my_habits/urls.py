from django.urls import path, include
from rest_framework.routers import DefaultRouter

from my_habits.views import HabitViewSet

app_name = 'my_habits'

# Создаем объект DefaultRouter для автоматической генерации URL-путей для представления HabitViewSet.
router = DefaultRouter()
router.register(r'my-habits', HabitViewSet, basename='my-habits')

urlpatterns = [
    path('', include(router.urls)),
] + router.urls
