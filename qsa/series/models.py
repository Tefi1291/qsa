from django.db import models
from django.contrib.auth.models import User


class Series(models.Model):
    # el id_serie corresponde con el id de la base de datos de tvdb
    # el cual deberia ser unico/ no editable desde el formulario
    id_serie = models.PositiveIntegerField() #editable=False
    serie_name = models.CharField(max_length=30)

    def __str__(self):
        return self.serie_name

    def traer_serie(self):
        # crear xml
        # enviar una peticion a la api de tvdb
        # llenar los campos
        #self.save()
        pass


class Season(models.Model):
    serie = models.ForeignKey(Series)
    id_season = models.PositiveIntegerField()
    languaje = models.CharField(max_length=2)
    #banner = models.ImageField()
    overview = models.CharField(max_length=250)
    aired = models.DateField()

    def __str__(self):
        return str(self.id_season)


class Episode(models.Model):
    season = models.ForeignKey(Season)
    id_episode = models.PositiveIntegerField()
    name_e = models.CharField(max_length=30)
    director = models.CharField(max_length=30)

    def __str__(self):
        return self.name_e


class ProfileUser (models.Model):
    user = models.OneToOneField(User)
    series = models.ManyToManyField(Series)
    #img = models.ImageField()

    def __str__(self):
        return self.user.username



