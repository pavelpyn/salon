# Generated by Django 3.1.2 on 2020-11-13 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='tel',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='contact',
            field=models.TextField(blank=True, max_length=1500, verbose_name='Напишите свой вопрос'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Ваше имя'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='theme',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Тема вопроса'),
        ),
    ]
