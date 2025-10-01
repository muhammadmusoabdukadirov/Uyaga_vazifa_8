from django.urls import path
from .views import AvtomobilList, AvtomobilDetail, EgasiList, EgasiDetail

urlpatterns = [
    # buham Avtomobil niki
    path('avtomobil/', AvtomobilList.as_view()),
    path('avtomobil/<int:pk>/', AvtomobilDetail.as_view()),

    # bunisiham Egasi niki
    path('egasi/', EgasiList.as_view()),
    path('egasi/<int:pk>/', EgasiDetail.as_view()),
]
