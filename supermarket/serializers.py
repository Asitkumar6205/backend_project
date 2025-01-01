from django.db.models.base import Model
from rest_framework import serializers
from .models import (SupermarketModel)

class SupermarketModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupermarketModel
        fields = "__all__"

