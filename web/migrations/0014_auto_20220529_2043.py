# Generated by Django 3.2.10 on 2022-05-29 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_rename_index_block_tag_visible_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=50, verbose_name='ФИО')),
                ('Phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('Email', models.CharField(max_length=50, verbose_name='Email')),
                ('Delivery_type', models.CharField(choices=[('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')], max_length=50, verbose_name='Тип доставки')),
                ('Region', models.CharField(max_length=50, verbose_name='Область')),
                ('City', models.CharField(max_length=50, verbose_name='Город')),
                ('Post_index', models.CharField(max_length=50, verbose_name='Почтовый индекс')),
                ('Address', models.CharField(max_length=50, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Заказы',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='Is_popular',
            field=models.BooleanField(default=False, verbose_name='Рекомендации'),
        ),
    ]