from .models import User, Customer
from .serializer import UserSerializer, CustomerSerializer
from rest_framework.viewsets import ModelViewSet


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = super(CustomerViewSet, self).get_queryset()
        return queryset
