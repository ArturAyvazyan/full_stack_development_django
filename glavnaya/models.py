from django.db import models

# Create your models here.

class Work(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    payment = models.URLField()
    videos = models.URLField()
    images_url = models.URLField()

    image_main = models.ImageField(upload_to = 'static/works/golova/')
    image_one = models.ImageField(upload_to = 'static/works/golova/')
    image_two = models.ImageField(upload_to = 'static/works/golova/')
    image_three = models.ImageField(upload_to = 'static/works/golova/')
    image_four = models.ImageField(upload_to = 'static/works/golova/')
    image_five = models.ImageField(upload_to = 'static/works/golova/')
    image_seven = models.ImageField(upload_to = 'static/works/golova/')
    image_eight = models.ImageField(upload_to = 'static/works/golova/')
    image_nine = models.ImageField(upload_to = 'static/works/golova/')
    
    def __str__(self):
        return self.name