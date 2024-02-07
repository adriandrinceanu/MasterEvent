from rest_framework import serializers
from .models import *

class SpeakerSerializer(serializers.HyperlinkedModelSerializer):
    # speaker_sessions = serializers.StringRelatedField(many=True)
    class Meta:
        model = Speaker
        fields = ['url', 'id', 'name', 'company', 'position', 'image', 'social_media', 'speaker_sessions']
        extra_kwargs = {
            'url': {'view_name': 'speaker-detail', 'lookup_field': 'pk'}
        }


class SessionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Session
        fields = ['url', 'id', 'name', 'description', 'stage', 'day', 'start_time', 'end_time', 'moderator', 'speakers', 'sponsored_by']
        extra_kwargs = {
            'url': {'view_name': 'session-detail', 'lookup_field': 'pk'}
        }

   

class DaySerializer(serializers.HyperlinkedModelSerializer):
    # sessions = SessionSerializer(many=True, read_only=True)

    class Meta:
        model = Day
        fields = ['url', 'id', 'name', 'date', 'sessions']
        extra_kwargs = {
            'url': {'view_name': 'day-detail', 'lookup_field': 'pk'}
        }

class StageSerializer(serializers.HyperlinkedModelSerializer):
    # days = DaySerializer(many=True, read_only=True)

    class Meta:
        model = Stage
        fields = ['url', 'id', 'name', 'days']
        extra_kwargs = {
            'url': {'view_name': 'stage-detail', 'lookup_field': 'pk'}
        }
        
        
class AgendaSerializer(serializers.HyperlinkedModelSerializer):
    # sessions = SessionSerializer(many=True, read_only=True)

    class Meta:
        model = Agenda
        fields = ['url', 'id', 'sessions']
        extra_kwargs = {
            'url': {'view_name': 'agenda-detail', 'lookup_field': 'pk'}
        }
        
class BrandSerializer(serializers.HyperlinkedModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = ['url', 'id', 'name', 'logo', 'sessions']
        extra_kwargs = {
            'url': {'view_name': 'brand-detail', 'lookup_field': 'pk'}
        }