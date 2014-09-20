from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'MiniFlash.views.home', name='home'),
    url(r'^register$', 'MiniFlash.views.register', name='register'),
    url(r'^overview', 'MiniFlash.views.overview', name='overview'),

    url(r'^admin/', include(admin.site.urls)),
    #remove log out confirmation step
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    (r'^accounts/', include('allauth.urls')),
)
