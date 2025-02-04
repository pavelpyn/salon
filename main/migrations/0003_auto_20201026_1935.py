# Generated by Django 3.1.2 on 2020-10-26 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_review_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='done',
            field=models.BooleanField(default=False, verbose_name='Активация'),
        ),
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, help_text='Добавить фото', upload_to='main/static/avatar/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='review',
            name='tel',
            field=models.CharField(blank=True, max_length=17, null=True, verbose_name='Номер телефона'),
        ),
    ]
