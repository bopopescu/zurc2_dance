from django.conf.urls import patterns, include, url

from django.conf import settings
from django.views.generic import TemplateView


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from core.views import HomeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zurczdance.views.home', name='home'),
    # url(r'^zurczdance/', include('zurczdance.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'ritmos/', include("dances.urls")),
    #url(r'sortear/' include("dances.urls")),
    url(r'^contas/', include("accounts.urls")),
    url(r'^entrar/$', "django.contrib.auth.views.login",
        {'template_name':'login.html'}, name='login'),
    url(r'^sair/$', "django.contrib.auth.views.logout",
        {'next_page':'/'}, name='logout'),
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^$', "core.views.home", name='home'),
    url(r'^contato/$', 'core.views.contact', name='contact'),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$',
            'django.views.static.serve', 
            {'document_root': settings.STATIC_ROOT}),

)