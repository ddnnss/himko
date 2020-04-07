from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Domain(models.Model):
    name = models.CharField('Поддомен маленькими буквами (например, msk)',max_length=30, blank=False, null=True)
    town = models.CharField('Город (например, Москва)',max_length=30, blank=False, null=True)
    townAlias = models.CharField('Склонение города (должно отвечать на вопрос ГДЕ, например, Москве)',
                                      max_length=30,
                                      blank=False,
                                      null=True)


    def __str__(self):
        return 'Поддомен для города {}'.format(self.town)

    class Meta:
        verbose_name = "Поддомен"
        verbose_name_plural = "Поддомены"

