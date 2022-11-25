from django.shortcuts import render

from rest_framework import viewsets
from quickstart.serializers import BandSerializer, ListingSerializer, VoitureSerializer
from quickstart.models import Band, Listing, Voiture

def list(request):
    return render(request, 'listings.html')

def ban(request):
    return render(request, 'bands.html')

def voit(request):
    return render(request, 'voitures.html')


class BandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    #permission_classes = [permissions.IsAuthenticated]


class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    #permission_classes = [permissions.IsAuthenticated]
    
    
class VoitureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Voiture.objects.all()
    serializer_class = VoitureSerializer
    #permission_classes = [permissions.IsAuthenticated]