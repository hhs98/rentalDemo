from django.db import models


class Booking(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bookings'
        managed = True
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return self.product.name
