from django.urls import path

from rest_framework import routers

from users.views import UsersAPIViewSet, PaymentlListView

router = routers.SimpleRouter()
router.register('users', UsersAPIViewSet)

urlpatterns = [
    path("payments/list/", PaymentlListView.as_view(), name="payment_list"),
    ] + router.urls
