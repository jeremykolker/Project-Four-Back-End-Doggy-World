from rest_framework import serializers 
from .models import Dog

class DogSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Dog # tell django which model to use
        fields = ('id', 'name', 'age', 'breed', 'walk_time', 'feeding_instructions', 'photo_url') # tell django which fields to include
