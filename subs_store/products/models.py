from django.conf import settings
from django.db import models


# Create your models here.
class Orders(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goods = models.CharField(verbose_name='Товар', max_length=50)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    count = models.IntegerField(verbose_name='Количество')
    date_order = models.DateField(verbose_name='Дата покупки', auto_now_add=True)

    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'