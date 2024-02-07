from rest_framework import serializers
from .models import *



class SpeakerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Speaker
        fields = ['url', 'name', 'company', 'position', 'social_media', 'image']
        extra_kwargs = {
            'url': {'view_name': 'speaker-detail', 'lookup_field': 'pk'}
        }

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ['name']

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ['name']


class SessionSerializer(serializers.ModelSerializer):
    stage = StageSerializer(read_only=True)
    day = DaySerializer(read_only=True)
    speakers =  SpeakerSerializer(source='speaker_set', many=True, read_only=True) 
    sponsored_by = BrandSerializer(read_only=True)

    class Meta:
        model = Session
        fields = ['name', 'description', 'stage', 'day', 'start_time', 'end_time',  'moderator', 'speakers', 'sponsored_by']

class AgendaSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True)
    class Meta:
        model = Agenda
        fields = '__all__'


------------------------
class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = ['id', 'name']

class SessionSerializer(serializers.ModelSerializer):
    speakers = SpeakerSerializer(many=True, read_only=True)

    class Meta:
        model = Session
        fields = ['id', 'name', 'speakers']

class DaySerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)

    class Meta:
        model = Day
        fields = ['id', 'date', 'sessions']

class StageSerializer(serializers.ModelSerializer):
    days = DaySerializer(many=True, read_only=True)

    class Meta:
        model = Stage
        fields = ['id', 'name', 'days']