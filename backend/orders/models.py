from django.db import models

class OrderStatus(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'order_status'

    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    total_price = models.FloatField()
    address_id = models.IntegerField()
    status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)
    user_id = models.ForeignKey('user.user', on_delete=models.CASCADE)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return f"Order {self.id} - {self.total_price} VND"
    
class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    item_price = models.FloatField()
    quantity = models.IntegerField()
    sub_total = models.FloatField()
    unit_price = models.FloatField()
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product_id = models.ForeignKey('product.product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'order_detail'

    def __str__(self):
        return f"Order Detail {self.id} - Quantity: {self.quantity}"
    
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=300)
    date = models.DateField()
    vote = models.IntegerField()
    product_id = models.ForeignKey('product.product', on_delete=models.CASCADE)
    user_id = models.ForeignKey('user.user', on_delete=models.CASCADE)

    class Meta:
        db_table = 'review'

    def __str__(self):
        return f"Review {self.id} - {self.vote} stars"

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    user_id = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        db_table = 'cart'

    def __str__(self):
        return f"Cart {self.id} - User {self.user_id} - Product {self.product_id}"