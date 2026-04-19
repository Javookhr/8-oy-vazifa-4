from django.urls import path
from .views import CarListCreateView,CarUpdateDestroyView

urlpatterns = [
    path('cars/',CarListCreateView.as_view(),name='cars'),
    path('cars/<int:pk>',CarUpdateDestroyView.as_view(),name='car-detail')

]