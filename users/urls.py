from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

app_name = 'users'

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Получение JWT-токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Обновление JWT-токена
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  # Проверка JWT-токена
]