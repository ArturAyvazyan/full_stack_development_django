from django.db import models

# Create your models here.

class Zakaz(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    payment = models.URLField()
    
    
    def __str__(self):
        return self.name