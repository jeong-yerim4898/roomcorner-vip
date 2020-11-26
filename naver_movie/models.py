from django.db import models
from django.conf import settings

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
        
class Movie(models.Model):
    title = models.CharField(max_length=30)
    rank = models.FloatField()
    movie_id = models.IntegerField()
    audience = models.FloatField()
    poster_url = models.TextField()
    overview = models.TextField()
    original_lang = models.CharField(max_length=50)
    video_id = models.CharField(max_length=500)
    genre = models.ManyToManyField(Genre,symmetrical=False,related_name='movie')
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies',blank=True)
   
class Comment(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="movie")
    content = models.CharField(max_length=200)
    rank = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Corona(models.Model):
    city = models.CharField(max_length=50)
    corona_case = models.IntegerField()
