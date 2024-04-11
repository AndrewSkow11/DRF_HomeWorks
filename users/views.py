from rest_framework.viewsets import ModelViewSet
from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

class UsersAPIViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PaymentlListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = ['course', 'lesson', 'payment_type']
    ordering_fields = ['date']