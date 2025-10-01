from rest_framework import generics
from .models import Avtomobil, Egasi
from .serializers import AvtomobilSerializer, EgasiSerializer

# bu Avtomobil niki
class AvtomobilList(generics.ListCreateAPIView):
    queryset = Avtomobil.objects.all()
    serializer_class = AvtomobilSerializer

class AvtomobilDetail(generics.RetrieveAPIView):
    queryset = Avtomobil.objects.all()
    serializer_class = AvtomobilSerializer

# bu Egasi niki 
class EgasiList(generics.ListAPIView):
    queryset = Egasi.objects.all()
    serializer_class = EgasiSerializer

class EgasiDetail(generics.RetrieveAPIView):
    queryset = Egasi.objects.all()
    serializer_class = EgasiSerializer
