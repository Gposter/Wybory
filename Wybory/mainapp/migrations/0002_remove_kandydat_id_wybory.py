# Generated by Django 2.0.5 on 2018-06-05 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kandydat',
            name='id_wybory',
        ),
    ]
