# Generated by Django 3.2.10 on 2022-04-16 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Availability',
            field=models.BooleanField(default=False, verbose_name='Наличие'),
        ),
    ]