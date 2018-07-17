from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)

class Categories(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100) #slug=fetch--many record & id=fetch-single record

    def __str__(self):
        return self.name



class Products(models.Model):
    category=models.ForeignKey(Categories)
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,null=True)
    description=models.TextField(blank=True)
    pic=models.FileField(upload_to='pic',null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
class Cart(models.Model):
    product=models.ForeignKey(Products)
    total_price=models.FloatField(null=True)
    quantity=models.IntegerField(null=True)
    about=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.product.name
class Ord(models.Model):
    n=models.CharField(max_length=100,null=True)
    l=models.CharField(max_length=100,null=True)
    e=models.EmailField(null=True)
    p=models.IntegerField(null=True)
    a=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.n

class Cust(models.Model):
    na=models.CharField(max_length=100,null=True)
    ln=models.CharField(max_length=100,null=True)
    em=models.EmailField(null=True)
    ph=models.IntegerField(null=True)
    ad=models.CharField(max_length=100,null=True)

    f=models.CharField(max_length=100,null=True)
    s=models.CharField(max_length=100,null=True)
    el=models.CharField(max_length=100,null=True)
    d=models.IntegerField(null=True)
    pt=models.IntegerField(null=True)
    mc=models.CharField(max_length=100,null=True)
    #pict=models.FileField(upload_to='pic',null=True)

    def __str__(self):
        return self.na
