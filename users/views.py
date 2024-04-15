from rest_framework.viewsets import ModelViewSet
from users.models import User, Payment
from users.serializers import UserPaymentSerializer, PaymentSerializer, UserSerializer
from rest_framework.filters import SearchFilter
import django_filters.rest_framework

from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
)


class UsersPaymentsAPIViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserPaymentSerializer


class PaymentlListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter,
                       django_filters.rest_framework.DjangoFilterBackend]

    filterset_fields = ['course', 'lesson', 'payment_type']
    ordering_fields = ['date', ]


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
