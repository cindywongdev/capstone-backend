from .models import Listing, Request
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ListingSerializer, RequestSerializer


# Create your views here.
class ListingViewSet(viewsets.ModelViewSet):
    # main query for index route
    queryset = Listing.objects.all()
    # serializer class for serializing output
    serializer_class = ListingSerializer
    # option permission class to set permission level
    # Could be [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

## how do I make views for the 'many' model of a one to many relationship?
class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.AllowAny]