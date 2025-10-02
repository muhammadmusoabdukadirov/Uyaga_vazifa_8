from django.urls import path
from .views import AvtomobilAPIView, EgasiAPIView

urlpatterns = [
    
    path('avtomobil/', AvtomobilAPIView.as_view()),
    path('avtomobil/<int:pk>/', AvtomobilAPIView.as_view()),
    path('egasi/', EgasiAPIView.as_view()),
    path('egasi/<int:pk>/', EgasiAPIView.as_view()),
]

