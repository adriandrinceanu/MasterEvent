from django.contrib import admin
from .models import *

class SessionInline(admin.TabularInline):
    model = Session.speakers.through

class SpeakerAdmin(admin.ModelAdmin):
    inlines = [
        SessionInline,
    ]

admin.site.register(Speaker, SpeakerAdmin)
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    def speakers_display(self, obj):
        return ', '.join([speaker.name for speaker in obj.speakers.all()])
    
    list_display = ('stage', 'day', 'start_time', 'end_time', 'name', 'moderator', 'sponsored_by','speakers_display')
    list_filter = ('stage', 'day', 'speakers', 'sponsored_by')
    # Add any additional admin functionalities as needed

admin.site.register(Brand)

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # Add any additional admin functionalities as needed

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # Add any additional admin functionalities as needed
admin.site.register(Agenda)


