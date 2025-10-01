from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Avtomobil(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Avtomobil nomi")
    marka = models.CharField(max_length=100, verbose_name="Markasi")
    yil = models.PositiveIntegerField(verbose_name="Ishlab chiqarilgan yil")
    rang = models.CharField(max_length=50, verbose_name="Rangi")
    narx = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Narxi")
    dvigatel = models.CharField(max_length=50, verbose_name="Dvigatel turi")
    yurgan_km = models.PositiveIntegerField(verbose_name="Yurgan masofasi (km)")

    class Meta:
        verbose_name = "Avtomobil"
        verbose_name_plural = "Avtomobillar"

    def __str__(self):
        return f"{self.marka} {self.nom} ({self.yil})"


class Egasi(models.Model):
    ism = models.CharField(max_length=100, verbose_name="Egasi ismi")
    familiya = models.CharField(max_length=100, verbose_name="Egasi familiyasi")
    yosh = models.PositiveIntegerField(verbose_name="Yoshi")
    telefon = models.CharField(max_length=20, verbose_name="Telefon raqami")
    manzil = models.CharField(max_length=200, verbose_name="Manzili")
    avtomobil = models.ForeignKey(Avtomobil, on_delete=models.CASCADE, related_name="egalar")

    class Meta:
        verbose_name = "Avtomobil egasi"
        verbose_name_plural = "Avtomobil egalari"

    def __str__(self):
        return f"{self.ism} {self.familiya}"
