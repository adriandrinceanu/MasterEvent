from django.contrib import admin
from .models import *



class SessionInline(admin.TabularInline):
    model = Session.speakers.through

class SpeakerAdmin(admin.ModelAdmin):
    inlines = [SessionInline]

class SessionAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ('speakers',)

class DayAdmin(admin.ModelAdmin):
    list_display = ['name', 'date']
    filter_horizontal = ['sessions']

class StageAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ['days']

class AgendaAdmin(admin.ModelAdmin):
    filter_horizontal = ['sessions']

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Session, SessionInline)
admin.site.register(Day, DayAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Brand, BrandAdmin)
