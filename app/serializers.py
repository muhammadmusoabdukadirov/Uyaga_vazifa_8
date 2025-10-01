from rest_framework import serializers
from .models import Avtomobil, Egasi

class AvtomobilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avtomobil
        fields = "__all__"


class EgasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Egasi
        fields = "__all__"


# Bu zo`r usul ekan domla ham osson ekan