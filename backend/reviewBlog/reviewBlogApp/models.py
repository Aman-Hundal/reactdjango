import email
from django.db import models
from django.forms import IntegerField

# Create your models here.
class User(models.Model):
  email = models.EmailField(max_length=254)
  username = models.CharField(max_length=30)
  password = models.CharField(max_length=15)

class Post(models.Model):
  RATINGS_CHOICES = [
    (0, 'Dont watch'),
    (1, 'Bad'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Great'),
    (5, 'Outstanding')
  ]
  movie_title = models.CharField(max_length=100)
  post_date = models.DateField(auto_now_add=True)
  rating = models.IntegerField(choices = RATINGS_CHOICES, default = 0)
  review = models.TextField()
  movie_image = models.URLField(max_length=1000)
  user = models.ForeignKey(User, on_delete=models.CASCADE)


