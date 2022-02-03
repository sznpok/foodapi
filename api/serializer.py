from rest_framework import serializers
from .models import CategoryMenu,FoodType,Orders,SubCategoryMenu,Table,TableType,TimeForOrder

class FoodTypeSerializer(serializers.ModelSerializer):
    type = serializers.CharField(max_length=20)
    class Meta:
        model = FoodType
        fields = "__all__"
    

class CategoryMenuSerializer(serializers.ModelSerializer):
    menu = serializers.CharField(max_length=30,)
    class Meta:
        model = CategoryMenu
        fields = ['foodTypeId','menu']
