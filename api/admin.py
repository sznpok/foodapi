
from django.contrib import admin
from .models import FoodType,CategoryMenu, Orders, SubCategoryMenu, Table, TableType

admin.site.register(FoodType)
admin.site.register(CategoryMenu)
admin.site.register(SubCategoryMenu)
admin.site.register(TableType)
admin.site.register(Table)
admin.site.register(Orders)
