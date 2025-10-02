from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from .models import Avtomobil, Egasi
from .serializers import AvtomobilSerializer, EgasiSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Avtomobil uchun
# faqat o`qish uchun`
class AvtomobilAPIView(APIView):
    permission_classes = [IsAuthenticated]

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

# faqat qoshish uchun
    def post(self, request: Request, pk: int = None):
        if not pk:
            return Response(data={"Massage": "Method POST not allow"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            serializer = AvtomobilSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            avto = serializer.save()
            return Response(AvtomobilSerializer(avto).data, status=status.HTTP_201_CREATED)
        
# butunlay ozgartirish uchun
    def put(self, request, pk: int=None):
        if pk is None:
            return Response(
                {"massage": "ID (yani pk) kiritish kerak qo`zivoy"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            avto = Avtomobil.objects.get(pk=pk)
        except Exception as e:
            return Response({"error": "Avtomobil not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AvtomobilSerializer(instance=avto, data=request.data, partial=True if request.method == "PATCH" else False)
        serializer.is_valid(raise_exception=True)
        avto = serializer.save()
        return Response(AvtomobilSerializer(avto).data)

# qisman o`zgartirish uchun
    def patch(self, request, pk: int = None):
        return self.put(request, pk)


    # bu faqat o`chirish uchun
    def delete(self, request: Response, pk: int = None):
        if not pk:
            return Response(data={"Massage": "Method DELETE not allow"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            try:
                avto = Avtomobil.objects.get(pk=pk)
            except Exception as e:
                return Response(data={"Massage": "Avtomobil not found"}, status=status.HTTP_204_NO_CONTENT)
            
            avto.delete()
            return Response(data={"Massage": "Avtomobil delete secsesfull !!!"}, status=status.HTTP_204_NO_CONTENT)
# ____________________________________________________________________________
# Egasi uchun
class EgasiAPIView(APIView):
    permission_classes = [IsAdminUser]

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

    # faqat qoshish uchun
    def post(self, request: Request, pk: int = None):
            if not pk:
                return Response(data={"Massage": "Method POST not ellow"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            else:
                serializer = EgasiSerializer(data= Request.data)
                serializer.is_valid(raise_exception=True)
                avto = serializer.save()
                return Response(EgasiSerializer(avto).data, status=status.HTTP_201_CREATED)
            

    def put(self, request, pk: int = None):
        if pk is None:
            return Response(
                {"Massage": "ID (yangi pk) kiritish kerak qo`zivoy"}, status = status.HTTP_404_NOT_FOUND
            )
        try:
            avto = Avtomobil.objects.get(pk=pk)
        except Exception as e:
            return Response({"error": "Egasi not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = EgasiSerializer(instance=avto, data=request.data, partial = True if request.method == "PATCH" else False)
        serializer.is_valid(raise_exception=True)
        avto = serializer.save()
        return Response(EgasiSerializer(avto).data)
    
    def patch(self, request, pk: int = None):
        return self.put(request, pk)
    

    # bu faqat o`chirish uchun
    def delete(self, request: Response, pk: int = None):
        if not pk:
            return Response(data={"Massage": "Method DELETE not allow"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            try:
                avto = Egasi.objects.get(pk=pk)
            except Exception as e:
                return Response(data={"Massage": "Egasi not found"}, status=status.HTTP_204_NO_CONTENT)
            avto.delete()
            return Response(data={"Massage": "Egasi delete secsesfull !!!"}, status=status.HTTP_204_NO_CONTENT)