# Generated by Django 3.1.2 on 2020-11-13 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20201114_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masters',
            name='diploma',
        ),
        migrations.RemoveField(
            model_name='masters',
            name='photo',
        ),
        migrations.AddField(
            model_name='masters',
            name='diploma1',
            field=models.ImageField(blank=True, help_text='Добавить Диплом', upload_to='main/static/masters/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='masters',
            name='diploma2',
            field=models.ImageField(blank=True, help_text='Добавить Диплом', upload_to='main/static/masters/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='masters',
            name='diploma3',
            field=models.ImageField(blank=True, help_text='Добавить Диплом', upload_to='main/static/masters/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='masters',
            name='diploma4',
            field=models.ImageField(blank=True, help_text='Добавить Диплом', upload_to='main/static/masters/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='masters',
            name='photo1',
            field=models.ImageField(blank=True, help_text='Добавить фото', upload_to='main/static/masters/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='masters',
            name='photo2',
            field=models.ImageField(blank=True, help_text='Добавить фото', upload_to='main/static/masters/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='masters',
            name='photo3',
            field=models.ImageField(blank=True, help_text='Добавить фото', upload_to='main/static/masters/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='masters',
            name='photo4',
            field=models.ImageField(blank=True, help_text='Добавить фото', upload_to='main/static/masters/%Y/%m/%d'),
        ),
    ]
