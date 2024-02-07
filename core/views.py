from rest_framework import viewsets
from .models import Speaker, Session, Day, Stage, Agenda, Brand
from .serializers import *

class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    

class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    
