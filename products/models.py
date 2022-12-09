from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=120, default='code')
    name = models.CharField(max_length=120, default='name')
    type = models.CharField(max_length=120, default='type')
    availability = models.BooleanField(default=False)
    needing_repair = models.BooleanField(default=False)
    durability = models.IntegerField(default=0)
    max_durability = models.IntegerField(default=0)
    mileage = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(default=0)
    minimum_rent_period = models.IntegerField(default=0)

    class Meta:
        db_table = 'products'
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
