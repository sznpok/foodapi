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
         return f'{self.tableName}'


class TimeForOrder(models.Model):
    time_id = models.AutoField(primary_key=True)
    time = models.TimeField()
    
    def __str__(self):
        return f'{self.time}'
    def __unicode__(self):
        return "%s " % ( self.time(' %I:%M %p'))

class Orders(models.Model):
    orderId = models.AutoField(primary_key=True)
    categoryMenuId= models.ForeignKey(CategoryMenu,on_delete=models.CASCADE)
    subCategoryMenuId= models.ForeignKey(SubCategoryMenu,on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True,null=True)
    tableId = models.ForeignKey(Table,on_delete=models.CASCADE)
    date = models.DateField(blank=True,null=True )
    time = models.ForeignKey(TimeForOrder, on_delete=models.CASCADE,blank=True,null=True)

    class Meta:
         unique_together = ['date', 'time', 'orderId']
         
    def __str__(self):
           return f'{self.orderId}'


