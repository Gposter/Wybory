# Generated by Django 2.0.5 on 2018-06-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_kandydat_id_wybory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kandydat',
            name='partia',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='kandydat',
            name='zdjecie',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='lista_k',
            name='liczba_gl',
            field=models.IntegerField(default=0),
        ),
    ]
