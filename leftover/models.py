from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Listing(models.Model):
    # name of food
    food_name = models.CharField(max_length=100)
    
    # date the listing is created
    listing_date = models.DateField(auto_now_add=True)
    
    # image url of the food
    # stretch goal: create option to upload image file(s) directly (use ImageField())
    img = models.URLField(max_length=300)
    
    # array of ingredients in food
    # not required
    ingredients = ArrayField(
        models.CharField(max_length=25, blank=True)
    )
    
    # array of potential common allergens
    # not required
    allergens = ArrayField(
        models.CharField(max_length=25, blank=True)
    )
    
    # how many days the food is good for
    # will decrement over time
    good_for_x_days = models.PositiveIntegerField()
    
    # number of servings the offered food constitutes
    # decreases as restaurant accepts request for food
    num_servings = models.PositiveIntegerField()
    
    # time that food should be picked up by
    pickup_by_time = models.DateTimeField()
    
    # whether food is expired
    # turns true when good_for_x_days equals 0
    is_expired = models.BooleanField(default=False)
    
    # whether number of servings is > 0
    is_out_of_food = models.BooleanField(default=False)
    
    # name of restaurant (creator of listing)
    restaurant = models.CharField(max_length=30, default="Cindy's Restaurant")
    
    
class Request(models.Model):
    # name of user who made the request
    username = models.CharField(max_length=30)
    
    # whether user is an organization or an individual
    is_org = models.BooleanField()
    
    # number of servings being requested
    # must be equal to or lower than available servings
    num_servings = models.PositiveIntegerField()
    
    # status of request
    # is 1 of 3: pending, accepted, denied
    status = models.CharField(max_length=10, default="pending")
    
    # the specific listing that request is for
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)