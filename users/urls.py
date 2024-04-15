from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import routers

from users.apps import UsersConfig
from users.views import UsersPaymentsAPIViewSet, PaymentlListView, UserListAPIView, UserCreateAPIView

app_name = UsersConfig.name

router = routers.SimpleRouter()
router.register('users-payment', UsersPaymentsAPIViewSet)

urlpatterns = [
    path("payments/list/", PaymentlListView.as_view(), name="payment_list"),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('users/create/', UserCreateAPIView.as_view(), name='users_create'),
    path('users/list/', UserListAPIView.as_view(), name='users_list'),

] + router.urls



