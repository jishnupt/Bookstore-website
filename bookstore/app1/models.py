from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True)
    ROLE_CHOICE = (
        ('admin','admin'),
        ('user','user')
    )
    role = models.CharField(max_length=50,choices=ROLE_CHOICE,default='user')

class Books(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=True)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=40)
    review = models.CharField(max_length=50)
    image = models.ImageField(upload_to='books')

    def __str__(self):
        return self.name

class Add_cart(models.Model):
    b_name = models.ForeignKey(Books,on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    userr = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

