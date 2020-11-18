# Generated by Django 3.1.2 on 2020-11-13 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_service_price_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price_1',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Цены(от 25 до 40см)'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price_2',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Цены(от 25 до 40см)'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price_3',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Цены(от 25 до 40см)'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price_4',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Цены(от 40 и выше)'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price_man',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Мужская стрижка, стоимость работы без материалов'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price_man_all',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Мужская стрижка, стоимость работы'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price_man_material',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Мужская стрижка, расходные материалы'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price_nm_1',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Цены без расходных материалов1'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price_nm_2',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Цены без расходных материалов2'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price_nm_3',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Цены без расходных материалов3'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price_nm_4',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True, verbose_name='Цены без расходных материалов4'),
        ),
    ]
