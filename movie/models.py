from django.db import models
from django.urls import reverse


# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title
    



class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='movie_pic')
    slug = models.SlugField(blank=True)

    video = models.FileField(upload_to='movie_video')
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title



