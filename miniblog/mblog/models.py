from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class blogPost(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email   = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    date    = models.DateTimeField(auto_now_add=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'Profile')
    image = models.ImageField(upload_to='pics', default='default.jpg')

    def __str__(self):
        return f"{self.user.username} Profile"
    