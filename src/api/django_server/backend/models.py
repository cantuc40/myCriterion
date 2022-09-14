from django.db import models

# Create your models here.

class Film(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=60, default='')
    genre = models.CharField(max_length=25, default='')
    year = models.IntegerField(max_length=4, default=0)
    country = models.CharField(max_length=25, default='')
    director = models.CharField(max_length=40, default='')
    spine_number = models.IntegerField(max_length=5000, default=0)
    ratio = models.CharField(max_length=25, default='')
    studio = models.CharField(max_length=25, default='')
    mpaa_rating = models.CharField(max_length=5, default='')
    box_cover_url = models.CharField(max_length=2000, default='')

    class Meta:
        ordering = ['created']

    
    