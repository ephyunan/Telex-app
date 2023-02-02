from rest_framework import serializers
from .models import Tutor


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ('username','email')