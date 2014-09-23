from django.conf.urls import url, patterns

urlpatterns = patterns('Project.views',
    url(r'^projects$', 'my_projects', name='my_projects'),
    url(r'^projects/add$', 'add_project', name='add_project'),
    url(r'^projects/(?P<id>\d+)$$', 'project_detail', name='project_detail'),
    url(r'^projects/edit/(?P<id>\d+)$$', 'edit_project', name='edit_project'),
)