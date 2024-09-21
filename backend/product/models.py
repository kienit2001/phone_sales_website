from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True) 
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=300)
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name 
    
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    logo = models.CharField(max_length=255)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'brand'

    def __str__(self):
        return self.name

class Product(models.Model):
    description = models.CharField(max_length=255) 
    discount = models.IntegerField()
    image = models.CharField(max_length=255)
    in_stock = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)
    price_code = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    short_description = models.CharField(max_length=255)
    sold_quantity = models.IntegerField(default=0)
    brand_id = models.ForeignKey('brand', on_delete=models.CASCADE)
    category_id = models.ForeignKey('category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name 