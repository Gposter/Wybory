# Generated by Django 2.0.5 on 2018-06-07 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20180607_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kandydat',
            name='zdjecie',
            field=models.ImageField(blank=True, upload_to='mainapp/static/img'),
        ),
    ]