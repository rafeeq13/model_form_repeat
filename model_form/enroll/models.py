from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=70,blank=True)
    email=models.EmailField(max_length=20)
    address=models.CharField(max_length=30)

