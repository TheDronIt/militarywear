# Generated by Django 3.2.10 on 2022-05-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_auto_20220529_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Is_popular',
        ),
        migrations.AddField(
            model_name='product',
            name='Recommendations',
            field=models.CharField(choices=[('Отображать', 'Отображать'), ('Не отображать', 'Не отображать')], default='Не отображать', max_length=50, verbose_name='Рекомендации'),
        ),
    ]
