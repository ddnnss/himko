from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.template.loader import render_to_string
import settings

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
    doc = models.FileField('Доки', blank=True,null=True,upload_to='docs/')

    def is_doc(self):
        if self.doc:
            print(self.doc.url)
            return self.doc.url
        else:
            return False




def order_ps(sender, instance, **kwargs):
    msg_html = render_to_string('email/order.html', {'user': instance.name,
                                                     'phone': instance.phone,
                                                     'email': instance.email,
                                                     'id': instance.id,
                                                     'order': instance.order,
                                                     'doc':instance.is_doc()})
    send_mail('Новый заказ на сайте specsintez-pro.ru', None, 'info@specsintez-pro.ru', ['igor@equip-master.ru'],
              fail_silently=False, html_message=msg_html)

post_save.connect(order_ps, sender=Order)