from django.contrib import admin
from .models import Avtomobil, Egasi

@admin.register(Avtomobil)
class AvtomobilAdmin(admin.ModelAdmin):
    list_display = ("id", "nom", "marka", "yil", "rang", "narx", "dvigatel", "yurgan_km")
    search_fields = ("nom", "marka", "rang")
    list_filter = ("yil", "rang", "marka")


@admin.register(Egasi)
class EgasiAdmin(admin.ModelAdmin):
    list_display = ("id", "ism", "familiya", "yosh", "telefon", "manzil", "avtomobil")
    search_fields = ("ism", "familiya", "telefon")
    list_filter = ("yosh", "manzil")
