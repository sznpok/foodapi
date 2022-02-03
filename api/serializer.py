from rest_framework import serializers
from .models import CategoryMenu,FoodType,Orders,SubCategoryMenu,Table,TableType,TimeForOrder

class FoodTypeSeralizer(serializers.ModelSerializer):
    type = serializers.CharField(max_length=20)
    class Meta:
        model = FoodType
        fields = "__all__"
    