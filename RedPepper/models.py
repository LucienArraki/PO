from django.db import models
from django.utils import timezone


# Create your models here.
class Klient(models.Model):
    idK = models.AutoField(primary_key=True)
    login = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.login


class Platnosc(models.Model):
    idP = models.AutoField(primary_key=True)
    rodzaj = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.rodzaj


class Skladniki(models.Model):
    idS = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default=" ")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Oferta(models.Model):
    idO = models.AutoField(primary_key=True)
    type = models.CharField(max_length=200, default="pizza")
    name = models.CharField(max_length=200)
    info = models.ManyToManyField(Skladniki)
    priceSmall = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    priceBig = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Zamówienie(models.Model):
    idK = models.AutoField(primary_key=True)
    klient = models.ManyToManyField(Klient)
    zamowienia = models.ManyToManyField(Oferta)
    Platnosc = models.ManyToManyField(Platnosc)
    created_date = models.TimeField(timezone.now())

    class Meta:
        ordering = ('created_date',)

    def __str__(self):
        return str(self.created_date)
