from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from forms import ProjectForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from models import Project

@login_required
def my_projects(request):
	my_projects = Project.objects.filter(participants__id__exact=request.user.id)
	return render_to_response('authenticated/project/my_projects.html', locals(), context_instance=RequestContext(request))

@login_required
def add_project(request):
	if request.method == "POST":
		form = ProjectForm(request.POST, user=request.user)
		if form.is_valid():
			form.save(request)
			messages.success(request, 'Project created successfully.')
			return HttpResponseRedirect(reverse('my_projects'))
	else:
		form = ProjectForm()
	return render_to_response('authenticated/project/add_project.html', locals(), context_instance=RequestContext(request))