from django.db import models

# Create your tables
class Users(models.Model):
    Username = models.CharField(max_length=200)
    Password = models.CharField(max_length=16)
    Email = models.CharField(max_length=200)

class Transaction(models.Model):
    Trans_Desc = models.TextField()
    Trans_Date = models.DateTimeField()
    Trans_Type = models.CharField(max_length=50)
    Trans_Loc = models.CharField(max_length=150)
    Trans_Amnt = models.DecimalField(decimal_places=2, max_digits=150)
