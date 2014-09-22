from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def my_projects(request):
	return render_to_response('authenticated/project/my_projects.html', locals(), context_instance=RequestContext(request))