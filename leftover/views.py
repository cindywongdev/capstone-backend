from .models import Listing
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ListingSerializer


# Create your views here.
class ListingViewSet(viewsets.ModelViewSet):
    # main query for index route
    queryset = Listing.objects.all()
    # serializer class for serializing output
    serializer_class = ListingSerializer
    # option permission class to set permission level
    # Could be [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
