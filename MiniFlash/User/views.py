from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from forms import UserSettingsForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from models import CustomUser


@login_required
def user_settings(request):
	if request.method == "POST":
		form = UserSettingsForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save(request)
			return HttpResponseRedirect(reverse('user_settings'))
	else:
		form = UserSettingsForm(instance=request.user)
	return render_to_response('authenticated/user/user_settings.html', locals(), context_instance=RequestContext(request))