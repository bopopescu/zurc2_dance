# encoding: utf-8

from django import forms

from models import Rhythm, DanceStep


class RhythmForm(forms.ModelForm):

	class Meta:
		model = Rhythm
		# exclude = ['rhythm']

class DanceStepForm(forms.ModelForm):

	class Meta:
		model = DanceStep
		exclude = ['rhythm'] 

