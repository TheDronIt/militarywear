# Generated by Django 3.2.10 on 2022-04-23 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20220423_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='product_size',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
