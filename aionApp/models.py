# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class watche(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default=0) 
    quantity = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0)
    use = models.IntegerField(default=0) 
    picture = models.ImageField(upload_to='items/%Y/%m/%d/', default='items/default_item.jpg')
    
class review(models.Model):
    watch=models.ForeignKey(watche, on_delete=models.CASCADE)
    reviews= models.CharField(max_length=255)
    
class user(models.Model):
    user_id = models.IntegerField(default=0)
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    mi = models.CharField(max_length=3)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
class addresse(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    addresstype=models.IntegerField(default=1)
    hnum=models.IntegerField(default=0)
    street = models.CharField(max_length=255)
    subdivision = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal =models.IntegerField(default=0)
    country = models.CharField(max_length=255)
    

class checkout(models.Model):
    users=models.ForeignKey(user, on_delete=models.CASCADE)
    cardnumber=models.IntegerField()
    secnumber=models.IntegerField()
    total=models.FloatField(default=0)
    
class role(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    roletype=models.IntegerField(default=0)
    
class sale(models.Model):
    watch=models.ForeignKey(watche, on_delete=models.CASCADE)
    totalsales=models.FloatField(default=0)
    sproducttype=models.FloatField(default=0)
    sproduct=models.FloatField(default=0)
    
    
    