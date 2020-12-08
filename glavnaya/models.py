from django.db import models

# Create your models here.

class Work(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    payment = models.URLField()
    videos = models.URLField()
    images_url = models.URLField()

    image_main = models.ImageField()
    image_one = models.ImageField()
    image_two = models.ImageField()
    image_three = models.ImageField()
    image_four = models.ImageField()
    image_five = models.ImageField()
    image_seven = models.ImageField()
    image_eight = models.ImageField()
    image_nine = models.ImageField()
    
    def __str__(self):
        return self.name