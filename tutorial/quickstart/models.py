from django.db import models
from datetime import datetime

#mon modele band
class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField()
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    
#mon modele listing
class Listing(models.Model):
    class ListingType(models.TextChoices):
        RECORDS = 'R'
        CLOTHING = 'C'
        POSTERS = 'P'
        MISC = 'M'       
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=5)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField()
    type = models.fields.CharField(choices=ListingType.choices, max_length=5)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

