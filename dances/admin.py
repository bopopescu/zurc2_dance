#encoding: utf-8

from django.contrib import admin
from models import Rhythm, DanceStep, Level

def mark_private(modeladmin, request, queryset):
	queryset.update(public=False)
	modeladmin.message_user(request, u'Rítmos atualizado com sucesso')
mark_private.short_description = 'Marcar itens selecionados como privado'

def mark_public(modeladmin, request, queryset):
	queryset.update(public=True)
	modeladmin.message_user(request, u'Rítmos atualizados com sucesso')
mark_public.short_description = 'Marcar itens selecionados como publico'

class RhythmAdmin(admin.ModelAdmin):

	list_display = ['name', 'public','dancestep_count']
	search_fields = ['name']
	actions = [mark_private,mark_public]

admin.site.register(Rhythm, RhythmAdmin)

class LevelAdmin(admin.ModelAdmin):

	list_display = ['name']

admin.site.register(Level, LevelAdmin)

class DanceStepAdmin(admin.ModelAdmin):

	list_display = ['name','rhythm']
	search_fields = ['rhythm__name']
	
admin.site.register(DanceStep, DanceStepAdmin)