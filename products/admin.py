from django.contrib import admin
from .models import Product, Condition, BodySystem

admin.site.register(Product)
admin.site.register(Condition)
admin.site.register(BodySystem)
