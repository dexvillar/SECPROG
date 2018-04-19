# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import user, watche, review, billing_addres, shipping_addres, checkout, buy_watche, login_log, product_log, account_log

# Register your models here.

admin.site.register(user)
admin.site.register(watche)
admin.site.register(review)
admin.site.register(billing_addres)
admin.site.register(shipping_addres)
admin.site.register(checkout)
admin.site.register(buy_watche)
admin.site.register(login_log)
admin.site.register(product_log)
admin.site.register(account_log)
