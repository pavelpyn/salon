# Generated by Django 3.1.2 on 2020-10-26 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
