from django.shortcuts import render

from rest_framework import viewsets
from quickstart.serializers import BandSerializer, ListingSerializer
from quickstart.models import Band, Listing

def lang(request):
    return render(request, 'listings.html')

def frame(request):
    return render(request, 'bands.html')

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