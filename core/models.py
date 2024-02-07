from django.db import models

    
class Speaker(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='speakers_images/', null=True)
    social_media = models.URLField()
    
    def __str__(self):
        return self.name
    
class Session(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    stage = models.ForeignKey('Stage', on_delete=models.CASCADE)
    day = models.ForeignKey('Day', on_delete=models.CASCADE)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    moderator = models.ForeignKey(Speaker, related_name='moderated_sessions', on_delete=models.CASCADE,null=True, blank=True)
    speakers = models.ManyToManyField(Speaker, related_name='speaker_sessions')
    sponsored_by = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='sponsored_sessions')

    def __str__(self):
        return self.name    
    
    
class Day(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    sessions = models.ManyToManyField(Session, related_name='days')
    
    def __str__(self):
        return self.name    
    
class Stage(models.Model):
    name = models.CharField(max_length=200)
    days = models.ManyToManyField(Day, related_name='stages')    
    
    def __str__(self):
        return self.name


class Agenda(models.Model):
    sessions = models.ManyToManyField(Session)

    def __str__(self):
        return f'Agenda {self.id}'
    
class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='brands/', blank=True, null=True)

    def __str__(self):
        return self.name    






