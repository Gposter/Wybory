# Generated by Django 2.0.5 on 2018-06-11 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20180607_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='lista',
            name='czy_glos',
            field=models.IntegerField(default=0),
        ),
    ]