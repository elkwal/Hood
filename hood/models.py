from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.CharField(max_length= 50)
    neighbourhood_location = models.CharField(max_length=50)
    occupant_count=models.IntegerField()
    admin = models.ForeignKey(User,null=True,on_delete=models.CASCADE)

   

class User_Profile(models.Model):
    name = models.CharField(max_length=30)
    neighbourhood = models.ForeignKey(Neighbourhood,null = True,on_delete=models.CASCADE)
    email = models.EmailField()
    user_id = models.ForeignKey(User,null=True)
    profile_photo = models.ImageField(upload_to = 'gallary',blank=True,null=True)



class Business(models.Model):
    name = models.CharField(max_length=40)
    user = models.ForeignKey(User,null = True,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    email = models.EmailField()
    description = models.CharField(max_length=90)



class Post(models.Model):
    image = models.ImageField(upload_to='gallary/',blank=True,null= True)
    image_caption = models.TextField(max_length=200)
    profile = models.ForeignKey(User_Profile,null= True,blank= True)
    postdate = models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(User,null=True)


    class Meta:
        ordering=['-postdate']
