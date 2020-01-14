from django.db import models
from item.models import Item


class Cart(models.Model):
    client = models.CharField(max_length=255,blank=True,null=True)

    item = models.ForeignKey(Item, blank=True, null=True, default=None, on_delete=models.CASCADE,
                              verbose_name='Товар')
    number = models.IntegerField('Кол-во', blank=True, null=True, default=0)
    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзинах"

class Order(models.Model):
    name = models.CharField('Имя',max_length=255,blank=True,null=True)
    phone = models.CharField('Телефон', max_length=255, blank=True, null=True)
    email = models.CharField('Почта', max_length=255, blank=True, null=True)
    order = models.TextField('Заказ', blank=True, null=True)


