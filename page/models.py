from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db import models


# Create your models here.
from django.db.models.signals import post_save


import settings


class Callback(models.Model):
    name = models.CharField('Имя',max_length=255,blank=True,null=True)
    phone = models.CharField('Телефон', max_length=255, blank=True, null=True)
    email = models.CharField('Почта', max_length=255, blank=True, null=True)
    item = models.CharField('Товар', max_length=255, blank=True, null=True)

    created_at = models.DateField('Дата', auto_now_add=True)


def callback_ps(sender, instance, **kwargs):
    msg_html = render_to_string('email/callback.html', {'id': instance.id,
                                                        'user': instance.name,
                                                        'phone': instance.phone,
                                                        'item': instance.item,
                                                        'email': instance.email})
    send_mail('Заполнена форма обратной связи на сайте specsintez-pro.ru', None, 'info@specsintez-pro.ru', ['igor@astrapromo.ru'],
              fail_silently=False, html_message=msg_html)

post_save.connect(callback_ps, sender=Callback)