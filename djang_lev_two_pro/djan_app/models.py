from django.db import models

# Create your models here.
class User(models.Model):
    First_Name = models.CharField(max_length = 264)
    Second_Name = models.CharField(max_length = 264)
    E_mail = models.EmailField(max_length = 264,unique = True)
