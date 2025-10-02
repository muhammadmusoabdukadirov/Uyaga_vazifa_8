from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from .models import Avtomobil, Egasi
from .serializers import AvtomobilSerializer, EgasiSerializer


# Avtomobil uchun
class AvtomobilAPIView(APIView):
    def get(self, request: Request, pk: int = None):
        if not pk:
            avtomobillar = Avtomobil.objects.all()
            serializer = AvtomobilSerializer(avtomobillar, many=True)
            return Response(serializer.data)
        else:
            try:
                avtomobil = Avtomobil.objects.get(pk=pk)
                serializer = AvtomobilSerializer(avtomobil)
                return Response(serializer.data)
            except Exception as e:
                return Response({"message": "Avtomobil topilmadi"}, status=status.HTTP_404_NOT_FOUND)


# Egasi uchun
class EgasiAPIView(APIView):
    def get(self, request: Request, pk: int = None):
        if not pk:
            egalari = Egasi.objects.all()
            serializer = EgasiSerializer(egalari, many=True)
            return Response(serializer.data)
        else:
            try:
                egasi = Egasi.objects.get(pk=pk)
                serializer = EgasiSerializer(egasi)
                return Response(serializer.data)
            except Exception as e:
                return Response({"message": "Egasi topilmadi"}, status=status.HTTP_404_NOT_FOUND)
