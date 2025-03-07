from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
       name_length = serializers.SerializerMethodField()
       class Meta:
              model = Movie
              fields = '__all__'
       
       def get_name_length(self,object):
           return len(object.name)

       def validate_name(self,value):
              if len(value) < 2:
                     raise serializers.ValidationError("Name too Short")
              return value
         
       def validate(self,data):
              if data["name"] == data["description"]:
                     raise serializers.ValidationError('Both name and discription are same')
              return data