# Generated by Django 3.1.2 on 2020-11-13 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20201114_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='masters',
            name='diploma',
            field=models.FileField(blank=True, help_text='Добавить Диплом', upload_to='main/static/masters/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='masters',
            name='photo',
            field=models.FileField(blank=True, help_text='Добавить фото', upload_to='main/static/masters/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='masters',
            name='comment',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание'),
        ),
        migrations.DeleteModel(
            name='Photos',
        ),
    ]
