from rest_framework import serializers
from .models import CategoryMenu,FoodType,Orders,SubCategoryMenu,Table,TableType,TimeForOrder

class FoodTypeSerializer(serializers.ModelSerializer):
    type = serializers.CharField(max_length=20)
    class Meta:
        model = FoodType
        fields = ["type"]
    
class CategoryMenuSerializer(serializers.ModelSerializer):
    menu = serializers.CharField(max_length=30,)
    class Meta:
        model = CategoryMenu
        fields = ['foodTypeId','menu']

class SubCategoryMenuSerializer(serializers.ModelSerializer):

    menuName = serializers.CharField(max_length=30,)
    unit = serializers.CharField(max_length=20)

    class Meta:
        model = SubCategoryMenu
        fields = "__all__"

class TableTypeSerializer(serializers.ModelSerializer):
    type = serializers.CharField(max_length=20)
    class Meta:
        model = TableType
        fields = "__all__"

class TableSerializer(serializers.ModelSerializer):
    tableName = serializers.CharField(max_length=20)
    class Meta:
        model = Table
        fields = "__all__"

class OrderSerialzer(serializers.ModelSerializer):
    quantity = serializers.IntegerField()
    class Meta:
        model = Orders
        fields = "__all__"