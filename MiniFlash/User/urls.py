from django.conf.urls import url, patterns

urlpatterns = patterns('User.views',
    url(r'^user$', 'user_settings', name='user_settings'),
)