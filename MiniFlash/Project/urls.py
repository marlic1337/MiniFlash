from django.conf.urls import url, patterns

urlpatterns = patterns('Project.views',
    url(r'^projects$', 'my_projects', name='my_projects'),
    url(r'^projects/add$', 'add_project', name='add_project'),
)