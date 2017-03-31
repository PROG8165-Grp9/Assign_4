from django.db import models

# Create your models here.
class Users(models.Model):
    Username = models.CharField(max_length=200)
    Password = models.TextField()
    Email = models.TextField()