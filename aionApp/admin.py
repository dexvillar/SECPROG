# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import watche, review, user, addresse, checkout, role, sale

admin.site.register(watche)
admin.site.register(review)
admin.site.register(user)
admin.site.register(addresse)
admin.site.register(checkout)
admin.site.register(role)
admin.site.register(sale)