from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.BigAutoField(primary_key= True)
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    profit_earned = models.DecimalField(max_digits=10, decimal_places=2)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=0)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    orderdttm = models.DateTimeField()
    is_received = models.BooleanField(default=False)
    is_cancel = models.BooleanField(default=False)

    def __str__(self):
        return self.name