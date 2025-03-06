from rest_framework import serializers
from watchlist_app.models import Movie

def cheack_description(value):
      if len(value) < 2 :
             raise serializers.ValidationError("discription is too short")
      return value

class MovieSerializer(serializers.Serializer):
       id = serializers.IntegerField(read_only=True)
       name = serializers.CharField()
       description = serializers.CharField(validators=[cheack_description])
       active = serializers.BooleanField()
       
       def create(self, validated_data):
              return Movie.objects.create(**validated_data)
       
       def update(self, instance, validated_data):
              instance.name=validated_data.get('name',instance.name)
              instance.description=validated_data.get('description',instance.description)
              instance.active=validated_data.get('active',instance.active)
              instance.save()
              return instance
       
       def validate_name(self,value):
              if len(value) < 2:
                     raise serializers.ValidationError("Name too Short")
              return value
         
       def validate(self,data):
              if data["name"] == data["description"]:
                     raise serializers.ValidationError('Both name and discription are same')
              return data