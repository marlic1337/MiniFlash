from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
	def signup(self, request, user):
		pass

	def __init__(self, *args, **kwargs):
		super(CustomSignupForm, self).__init__(*args, **kwargs)
		self.fields.pop('password2')
		self.fields.pop('username')
		self.fields['email'].label = ''
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['password1'].label = ''