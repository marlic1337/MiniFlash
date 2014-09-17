from allauth.account.forms import LoginForm

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].label = ''
        self.fields['password'].label = ''
        self.fields.pop('remember')
        self.fields['login'].widget.attrs['placeholder'] = 'Email'