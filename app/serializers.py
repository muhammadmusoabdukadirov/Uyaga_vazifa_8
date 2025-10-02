from rest_framework import serializers
from .models import Avtomobil, Egasi


class AvtomobilSerializer(serializers.ModelSerializer):
    nom = serializers.CharField(max_length=100)
    marka = serializers.CharField(max_length=100)
    yil = serializers.IntegerField()
    rang = serializers.CharField(max_length=50)
    narx = serializers.DecimalField(max_digits=12, decimal_places=2)
    dvigatel = serializers.CharField(max_length=50)
    yurgan_km = serializers.IntegerField()

    class Meta:
        model = Avtomobil
        fields = ["id","nom","marka","yil","rang","narx","dvigatel","yurgan_km"]


class EgasiSerializer(serializers.ModelSerializer):
    ism = serializers.CharField(max_length=100)
    familiya = serializers.CharField(max_length=100)
    yosh = serializers.IntegerField()
    telefon = serializers.CharField(max_length=20)
    manzil = serializers.CharField(max_length=200)
    avtomobil = serializers.PrimaryKeyRelatedField(queryset=Avtomobil.objects.all())

    class Meta:
        model = Egasi
        fields = ["id","ism","familiya","yosh","telefon","manzil","avtomobil"]
