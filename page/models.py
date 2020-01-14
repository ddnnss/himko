from django.db import models

# Create your models here.
class Callback(models.Model):
    name = models.CharField('Имя',max_length=255,blank=True,null=True)
    phone = models.CharField('Телефон', max_length=255, blank=True, null=True)
    email = models.CharField('Почта', max_length=255, blank=True, null=True)
    created_at = models.DateField('Дата', auto_now_add=True)

