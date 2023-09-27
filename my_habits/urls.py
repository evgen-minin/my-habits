from rest_framework.routers import DefaultRouter

from my_habits.views import HabitViewSet

app_name = 'my_habits'

router = DefaultRouter()
router.register(r'my-habits', HabitViewSet, basename='my-habits')

urlpatterns = [] + router.urls
