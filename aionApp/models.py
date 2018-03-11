# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

watch_choices = {
    ('0', 'Analog Watch'),
    ('1', 'Digital Watch'),
    ('2', 'Smart Watch'),
}

role_choices = {
    ('0', 'Product Manager'),
    ('1', 'Accounting Manager'),
    ('2', 'Administrator'),
    ('3', 'User'),
}

class billing_addres(models.Model):
    #user=models.ForeignKey(user, on_delete=models.CASCADE)
    house_number = models.IntegerField(default=0)
    street = models.CharField(max_length=255)
    subdivision = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    
    def __str__(self):
        return self.city
    
class shipping_addres(models.Model):
    #user=models.ForeignKey(user, on_delete=models.CASCADE)
    house_number = models.IntegerField(default=0)
    street = models.CharField(max_length=255)
    subdivision = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    
    def __str__(self):
        return self.city

class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_initial = models.CharField(max_length=3)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    role_type = models.CharField(max_length=16, choices=role_choices, default='3')
    billing_add=models.ForeignKey(billing_addres)
    shipping_add=models.ForeignKey(shipping_addres)
    
    def __str__(self):
        return self.last_name

class watche(models.Model):
    watch_id = models.PositiveIntegerField(default=0)
    user_id = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2048, default=0) 
    quantity = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    watch_type = models.CharField(max_length=16, choices=watch_choices, default='0')
    price = models.FloatField(default=0)
    picture = models.ImageField(upload_to = 'watchPictures/', default = 'media/no-img.jpg')

    def __str__(self):
        return self.name
    
class review(models.Model):
    watch_id = models.IntegerField(default = 0)
    reviews= models.CharField(max_length=255)
    
    def __str__(self):
        return self.reviews
    

    
class checkout(models.Model):
    user_id = models.PositiveIntegerField(default=0)
    card_number = models.IntegerField()
    security_number = models.IntegerField()
#    expiration_date = models.DateField(auto_now=False)
    total = models.FloatField(default=0)
    
    def __str__(self):
        return self.card_number
    
class sale(models.Model):
    watch_id = models.PositiveIntegerField(default=0)
    total_sales = models.FloatField(default=0)
    product_type = models.FloatField(default=0)
    product = models.FloatField(default=0)
    
    def __str__(self):
        return self.product
