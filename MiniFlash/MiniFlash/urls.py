from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'MiniFlash.views.home', name='home'),
    url(r'^register$', 'MiniFlash.views.register', name='register'),

    url(r'^admin/', include(admin.site.urls)),
    #(r'^accounts/', include('allauth.urls')),
)
