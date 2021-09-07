from django.db.models.options import IMMUTABLE_WARNING
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegisterView, ProfileUpdateView, ProfileView

app_name = 'api'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('get-profile/', ProfileView.as_view(), name='profile_get'),
    path('update-profile/', ProfileUpdateView.as_view(), name='profile_update'),
]
