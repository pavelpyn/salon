# Generated by Django 3.1.2 on 2020-11-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20201113_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price_man_material',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, verbose_name='Мужская стрижка, расходные материалы'),
        ),
    ]
