import imp
from django.contrib import admin
from .models import FoodType,CategoryMenu

admin.site.register(FoodType)
admin.site.register(CategoryMenu)
