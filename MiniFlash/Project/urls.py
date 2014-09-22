from django.conf.urls import url, patterns

urlpatterns = patterns('Project.views',
    url(r'^projects$', 'my_projects', name='my_projects'),
)