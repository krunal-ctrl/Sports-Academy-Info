# Generated by Django 3.1.2 on 2020-10-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0004_academy_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academy',
            name='city',
            field=models.CharField(default='', max_length=200),
        ),
    ]
