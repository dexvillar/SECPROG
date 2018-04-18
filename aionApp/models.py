# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django_countries.fields import CountryField
from passlib.hash import pbkdf2_sha256
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
    house_number = models.IntegerField(default=0)
    street = models.CharField(max_length=255)
    subdivision = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = CountryField()
    
    def __str__(self):
        return self.city
    
class shipping_addres(models.Model):
    house_number = models.IntegerField(default=0)
    street = models.CharField(max_length=255)
    subdivision = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = CountryField()
    
    def __str__(self):
        return self.city

class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    middle_initial = models.CharField(max_length=3)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    role_type = models.CharField(max_length=16, choices=role_choices, default='3')
    billing_add=models.ForeignKey(billing_addres, default=0)
    shipping_add=models.ForeignKey(shipping_addres, default=0)
    
    def verify_pass(self, raw_pass):
        return pbkdf2_sha256.verify(raw_pass, self.password)
    
    def __str__(self):
        return self.last_name

class watche(models.Model):
    watch_id = models.PositiveIntegerField(default=0)
    user_id = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2048, default=0) 
    stock = models.PositiveIntegerField(default=0)
    watch_type = models.CharField(max_length=16, choices=watch_choices, default='0')
    price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    picture = models.ImageField(upload_to = 'watchPictures/', default = 'media/no-img.jpg')

    def __str__(self):
        return self.name
    
class review(models.Model):
    watch_id = models.PositiveIntegerField(default = 0)
    user_id = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=255, default=0)
    reviews = models.CharField(max_length=2048)
    
    def __str__(self):
        return self.name

class checkout(models.Model):
    watch_id = models.PositiveIntegerField(default = 0)
    user_id = models.PositiveIntegerField(default=0)
    card_number = models.PositiveIntegerField(default=0)
    security_number = models.PositiveIntegerField(default=0)
    month = models.PositiveIntegerField(default=0)
    year = models.PositiveIntegerField(default=0)
    
    def __unicode__(self):
        return str(self.card_number)
    
class sale(models.Model):
    watch_id = models.PositiveIntegerField(default=0)
    total_sales = models.FloatField(default=0)
    product_type = models.FloatField(default=0)
    product = models.FloatField(default=0)
    
    def __str__(self):
        return self.product
    
class buy_watche(models.Model):
    watch_id = models.PositiveIntegerField(default=0)
    user_id = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=255, default=0)
    description = models.CharField(max_length=2048, default=0)
    price = models.FloatField(default=0)
    picture = models.ImageField(upload_to = 'watchPictures/', default = 'media/no-img.jpg')
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name

class login_log(models.Model):
    log= models.CharField(max_length=255, default=0)
    time= models.DateTimeField(auto_now_add=True, blank=True)
    date= models.DateField(auto_now_add=True, blank=True)
    username=models.CharField(max_length=255, default=0)
    location=models.CharField(max_length=255, default=0)
    action=models.CharField(max_length=255, default=0)
    result=models.CharField(max_length=255, default=0)
    
    def get_time(self):
        return self.time
    def get_date(self):
        return self.date
    def __str__(self):
        return self.log