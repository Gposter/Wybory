from django.db import models

# Create your models here.
class Wybory(models.Model):
    w =(
        ('t','tak'),
        ('n','nie'),
        )
    nazwa = models.CharField(max_length=20)
    data_pocz= models.DateTimeField(max_length=20)
    ilosc = models.IntegerField()
    wybor = models.CharField(max_length=2 , choices=w)
    data_koncowa=models.DateTimeField(max_length=20)


class Kandydat(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko =  models.CharField(max_length=20)
    partia = models.CharField(max_length=20 ,default=None)
    zdjecie = models.ImageField(upload_to='mainapp/static/img',blank=True)

class osoba_gl(models.Model):
    Pesel = models.CharField(max_length=10)
    haslo = models.CharField(max_length=20)

class Lista(models.Model):
    id_wybory = models.ForeignKey(Wybory,on_delete=models.CASCADE)
    id_osoba = models.ForeignKey(osoba_gl, on_delete=models.CASCADE)
    czy_glos = models.IntegerField(default=0)

class Lista_K(models.Model):
    id_wybory = models.ForeignKey(Wybory,on_delete=models.CASCADE)
    id_Kandynaci = models.ForeignKey(Kandydat,on_delete=models.CASCADE)
    liczba_gl = models.IntegerField(default=0)
