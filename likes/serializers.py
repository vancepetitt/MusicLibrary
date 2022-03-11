from rest_framework import serializers
from . import models
from .models import LikeCounter

class LikeCounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeCounter
        fields = ['like_count']