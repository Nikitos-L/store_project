from datetime import timedelta

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


ACTIVE_TYPES = (
        ('active', 'Active'),
        ('archive', 'Archive'),
    )

# Create your models here.
class Tariffs(models.Model):
    name_tariff = models.CharField(verbose_name='Тариф', max_length=50, unique=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=5, decimal_places=2)
    description = models.TextField(verbose_name='Описание')
    is_active = models.CharField(verbose_name='Состояние', choices=ACTIVE_TYPES,
                                    default=ACTIVE_TYPES[0][0])

    def __str__(self):
        return self.name_tariff

    class Meta:
        db_table = 'tariff'
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'


class UserSubscriptions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tariff = models.OneToOneField(Tariffs, on_delete=models.PROTECT)
    count_month = models.IntegerField(verbose_name='Количество месяцев', default=0)
    date_buy = models.DateField(verbose_name='Дата начала', auto_now=True, editable=False)

    @property
    def date_end(self):
        return self.date_buy + timedelta(days=self.count_month)

    class Meta:
        db_table = 'user_subscription'
        verbose_name = 'Подписка пользователя'
        verbose_name_plural = 'Подписки пользователей'

    def __str__(self):
        return f'User: {self.user.username}, Tariff: {self.tariff.name_tariff}'


class CustomUser(AbstractUser):
    phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',   # r'^\+?1?\d{9,15}$',
                message="Incorrect phone format."
            )
        ]
    )