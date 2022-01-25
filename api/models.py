from django.db import models

class FoodType(models.Model):
    type = models.CharField(max_length=20,blank=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

class CategoryMenu(models.Model):
    foodTypeId = models.ForeignKey(FoodType,related_name="category",on_delete=models.CASCADE)
    menu = models.CharField(max_length=30,null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.menu},{self.foodTypeId.type}'