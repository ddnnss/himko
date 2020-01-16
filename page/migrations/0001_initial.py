# Generated by Django 3.0.2 on 2020-01-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Callback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Почта')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
        ),
    ]
