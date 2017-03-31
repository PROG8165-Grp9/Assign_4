from django.db import models

# Create your models here.
class User(models.Model):
    Username = models.TextField()
    Password = models.TextField()
    Email = models.TextField()