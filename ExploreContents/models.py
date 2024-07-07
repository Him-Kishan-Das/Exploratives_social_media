from django.db import models

# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)


class post(models.Model):
    user_id = models.IntegerField()
    post_caption = models.TextField()
    post_timestamp = models.DateField(auto_now=True)
    post_image = models.ImageField(upload_to='post')
    post_likes = models.IntegerField()