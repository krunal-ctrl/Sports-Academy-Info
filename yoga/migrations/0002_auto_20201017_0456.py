# Generated by Django 3.1 on 2020-10-17 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yoga',
            name='contact_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='yoga',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
