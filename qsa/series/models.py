from django.db import models


class Series(models.Model):

    id_serie = models.PositiveIntegerField(primary_key=True)
    serie_name = models.CharField(max_length=30)

    def __str__(self):
        return self.serie_name


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

class User(models.Model):

    series = models.ManyToManyField(Series)
    name_u = models.CharField(max_length=30)

    def __str__(self):
        return self.name_u



