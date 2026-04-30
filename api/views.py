from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework import permissions

from .serializers import CarSerializer,RegisterSerializer, DriveSerializer, DriveHyperlinkedSerializer
from .models import Car, Drive

from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.prefetch_related('cars').all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.IsAuthenticated]

class CarListCreateView(ListCreateAPIView):
    queryset = Car.objects.select_related('owner').prefetch_related('drives').defer('year')
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

class CarUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.select_related('owner').all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

class DriveListCreateView(ListCreateAPIView):
    queryset = Drive.objects.select_related('car').only('id', 'name', 'phone', 'price', 'age', 'car__id', 'car__name')
    serializer_class = DriveSerializer
    permission_classes = [permissions.IsAuthenticated]

class DriveDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Drive.objects.select_related('car').defer('price')
    serializer_class = DriveHyperlinkedSerializer
    permission_classes = [permissions.IsAuthenticated]