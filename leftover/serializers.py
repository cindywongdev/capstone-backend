from .models import Listing
from rest_framework import serializers

# Listing serializer
class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # the model it will serialize
        model = Listing
        # the fields that should be included in the serialized output
        fields = ['id', 'food_name', 'listing_date', 'img', 'ingredients', 'allergens', 'good_for_x_days', 'num_servings', 'pickup_by_time', 'is_expired', 'is_out_of_food']