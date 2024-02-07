from rest_framework import serializers
from .models import *

class SpeakerSerializer(serializers.ModelSerializer):
    speaker_sessions = serializers.StringRelatedField(many=True)
    class Meta:
        model = Speaker
        fields = ['id', 'name', 'company', 'position', 'image', 'social_media', 'speaker_sessions']

class SessionSerializer(serializers.ModelSerializer):


    class Meta:
        model = Session
        fields = ['id', 'name', 'description', 'stage', 'day', 'start_time', 'end_time', 'moderator', 'speakers', 'sponsored_by']

   

class DaySerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)

    class Meta:
        model = Day
        fields = ['id', 'name', 'date', 'sessions']

class StageSerializer(serializers.ModelSerializer):
    days = DaySerializer(many=True, read_only=True)

    class Meta:
        model = Stage
        fields = ['id', 'name', 'days']
        
        
class AgendaSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)

    class Meta:
        model = Agenda
        fields = ['id', 'sessions']
        
class BrandSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = ['id', 'name', 'logo', 'sessions']