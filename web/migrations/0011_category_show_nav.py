# Generated by Django 3.2.10 on 2022-04-23 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_basket_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Show_nav',
            field=models.CharField(choices=[('Отображать', 'Отображать'), ('Не отображать', 'Не отображать')], default='Не отображать', max_length=50, verbose_name='Отображать в меню'),
        ),
    ]
