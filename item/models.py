from django.db import models

class Category(models.Model):
    name = models.CharField('Название категории', max_length=255, blank=False, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField('Изображение категории', upload_to='category_img/', blank=True)
    page_title = models.CharField('Название страницы SEO', max_length=255, blank=True, null=True)
    page_description = models.CharField('Описание страницы SEO', max_length=255, blank=True, null=True)
    page_keywords = models.TextField('Keywords SEO', blank=True, null=True)
    short_description = models.TextField('Краткое описание', blank=True)
    views = models.IntegerField('Просмотров', default=0)
    is_active = models.BooleanField('Отображать категорию ?', default=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     self.name_slug = slugify(self.name)
    #     super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return '%s ' % self.name

    class Meta:
        verbose_name = "Основная категория"
        verbose_name_plural = "Основные категории"


class Item(models.Model):

    category = models.ManyToManyField(Category, blank=True, null=True, db_index=True,verbose_name='Категория')
    name = models.CharField('Название товара', max_length=255, blank=False, null=True)
    image = models.ImageField('Картинка',upload_to='item/',blank=True, null=True)
    text1 = models.TextField(
        'Краткое описание товара (отображается в карточке товара)',
        blank=True, null=True)
    text2 = models.TextField(
        'Краткое описание товара (отображается в карточке товара)',
        blank=True, null=True)
    price = models.CharField('Цена', max_length=255, blank=True, null=True)

    def __str__(self):
        return 'id:%s %s ' % (self.id, self.name)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"