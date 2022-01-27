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

class SubCategoryMenu(models.Model):
    foodTypeId = models.ForeignKey(FoodType,on_delete=models.CASCADE)
    categoryMenuId= models.ForeignKey(CategoryMenu,on_delete=models.CASCADE)
    menuName = models.CharField(max_length=30,null=True,blank=True)
    image = models.ImageField(upload_to='images/menuItem')
    unit = models.CharField(max_length=20,null=True,blank=True)
    price = models.FloatField(max_length=10)

    def __str__(self):
        return self.menuName

class TableType(models.Model):
    type = models.CharField(max_length=20,blank=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

class Table(models.Model):
     tableTypeId = models.ForeignKey(TableType,on_delete=models.CASCADE)
     tableName = models.CharField(max_length=20,null=True,blank=True)
     updated = models.DateTimeField(auto_now=True)
     created = models.DateTimeField(auto_now_add=True)
     status = models.BooleanField(default=False)

     def __str__(self):
         return self.tableName

