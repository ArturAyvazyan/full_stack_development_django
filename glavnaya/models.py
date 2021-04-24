from django.db import models

# Create your models here.

class Zakaz(models.Model):
    work = models.CharField(max_length=225)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=225)
    otpravka = models.CharField(max_length=225)
    payment = models.CharField(max_length=225)
    koment = models.CharField(max_length=225)



    def __str__(self):
        return self.name