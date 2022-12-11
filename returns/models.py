from django.db import models


class Return(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='returns')
    from_date = models.DateField()
    to_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage_used = models.IntegerField(null=True, blank=True)
    needs_repair = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'returns'
        managed = True
        verbose_name = 'Return'
        verbose_name_plural = 'Returns'

    def __str__(self):
        return self.product.name
