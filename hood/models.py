from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length= 50)
    neighbourhood_location = models.CharField(max_length=50)
    occupant_count=models.IntegerField()
    admin = models.ForeignKey(User,null=True,on_delete=models.CASCADE)

