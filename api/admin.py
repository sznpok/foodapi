
from django.contrib import admin
from .models import FoodType,CategoryMenu, SubCategoryMenu

admin.site.register(FoodType)
admin.site.register(CategoryMenu)
admin.site.register(SubCategoryMenu)
