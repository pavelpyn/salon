# Generated by Django 3.1.2 on 2020-11-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20201113_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price_1',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Цены(до 15 см)'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price_2',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Цены(от 15 до 25 см)'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price_3',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Цены(от 25 до 40 см)'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price_4',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Цены(от 40 см и выше)'),
        ),
    ]
