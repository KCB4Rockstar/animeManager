from __future__ import unicode_literals
from django.db import models

# Create your models here.
from animeapp.animes import Anime

class Document(models.Model):
    csvFile = models.FileField(upload_to='')
