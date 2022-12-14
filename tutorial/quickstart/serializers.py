from django.contrib.auth.models import User, Group
from rest_framework import serializers

from quickstart.models import Band, Listing, Voiture


class BandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Band
        fields = ['name', 'genre', 'biography', 'year_formed', 'active', 'official_homepage']


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
        fields = ['title', 'description', 'sold', 'year', 'type', 'band']

class VoitureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Voiture
        fields = ['title', 'description', 'year']