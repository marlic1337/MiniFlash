from django.shortcuts import render_to_response
from django.template import RequestContext
from User.forms import CustomSignupForm
from User.login_form import CustomLoginForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def home(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('overview'))
	if request.method == "POST":
		form = CustomLoginForm(request.POST)
		if form.is_valid():
			print "test"
			form.login(request)
			return HttpResponseRedirect(reverse('home'))
	else:
		form = CustomLoginForm()
	return render_to_response('public/public_login.html', locals(), context_instance=RequestContext(request))

def register(request):
	if request.method == "POST":
		form = CustomSignupForm(request.POST)
		if form.is_valid():
			form.save(request)
			return HttpResponseRedirect(reverse('home'))
	else:
		form = CustomSignupForm()
	return render_to_response('public/public_register.html', locals(), context_instance=RequestContext(request))

@login_required
def overview(request):
	return render_to_response('authenticated/base.html', locals(), context_instance=RequestContext(request))