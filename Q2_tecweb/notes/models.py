from django.db import models

class Note(models.Model):
    # models.Model - herdando dessa classe
    # __init__() automático
    memo = models.CharField(max_length=500)

    def __str__(self):
        id = self.id
        string = ("'{0}'".format(id))
        return string