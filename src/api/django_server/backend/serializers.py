from dataclasses import fields
from rest_framework import serializers
from backend.models import Film
from django.contrib.auth.models import User


class FilmSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='film-highlight', format='html')

    class Meta:
        model = Film
        fields = ['url', 'id', 'owner', 'name', 'genre', 'year', 'country',
                  'director', 'spine_number', 'ratio', 'studio', 'mpaa_rating',
                  'box_cover_url' ]


#Turns User Instances into JSON files for output
class UserSerializer(serializers.HyperlinkedModelSerializer):
    films = serializers.HyperlinkedRelatedField(many=True, view_name='film-detail', read_only=True)

    #Display fields based on User Model
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'films']