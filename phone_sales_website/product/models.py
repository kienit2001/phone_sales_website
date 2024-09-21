from django.db import models

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
    brand_id = models.IntegerField()
    category_id = models.IntegerField()

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name 