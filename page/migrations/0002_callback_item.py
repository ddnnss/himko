# Generated by Django 3.0.2 on 2020-04-06 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='callback',
            name='item',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Товар'),
        ),
    ]
