from django.urls import path
from .views import CarListCreateView, CarUpdateDestroyView, RegisterView, DriveListCreateView, DriveDetailView, UserDetailView

urlpatterns = [
    path('cars/', CarListCreateView.as_view(), name='cars'),
    path('cars/<int:pk>/', CarUpdateDestroyView.as_view(), name='car-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('drives/', DriveListCreateView.as_view(), name='drives'),
    path('drives/<int:pk>/', DriveDetailView.as_view(), name='drive-detail'),
]