from rest_framework import serializers
from . import models

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = "__all__"
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = "__all__"