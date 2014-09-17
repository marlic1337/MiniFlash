from django.shortcuts import render_to_response
from django.template import RequestContext
from User.forms import CustomSignupForm
from User.login_form import CustomLoginForm

def home(request):
    form = CustomLoginForm()
    return render_to_response('public/public_login.html', locals(), context_instance=RequestContext(request))

def register(request):
    form = CustomSignupForm()
    return render_to_response('public/public_register.html', locals(), context_instance=RequestContext(request))