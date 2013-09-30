# encoding : utf-8 


from django.conf.urls import patterns, include, url

from .views import RhythmListView


urlpatterns = patterns('dances.views',
	url(r'^$', RhythmListView.as_view(), name='rhythms'),
	url(r'^passos/$', 'index_ds', name='dancesteps'),
	url(r'^(?P<pk>\d+)/$', "details", name='rhythms_details'),
	# url(r'^sorteado/$', "sorted", name='dancesteps_sorted'),
	url(r'^(?P<pk>\d+)/sorteado/$', "dancestep_sorted", name='dancesteps_sorted'),
	url(r'^novo-evento/$', 'create', name='rhythm_create'),
	url(r'^meus-ritmos/$', 'my', name='rhythm_my'),
	url(r'^(?P<pk>\d+)/alterar/$', "edit", name='rhythm_edit'),
)