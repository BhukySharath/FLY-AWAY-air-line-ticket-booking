from django.db import models

# Create your models here.

class Destination(models.Model):

    name =  models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)



class Sub(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


class Booked(models.Model):
    name=models.CharField(max_length=1000)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    destini = models.CharField(max_length=100)
    date = models.DateField()
    phno = models.BigIntegerField()