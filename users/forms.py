from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div


class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()
	terms=forms.BooleanField()
	class Meta:
		model=User
		fields=['username','email','password1','password2']
	def __init__(self,*args,**kwargs):
		super().__init__(*args, **kwargs)
		super(UserRegisterForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
            Field('password1',css_class='pswrds'),
            Field('password2',css_id='pswrd'))
		self.fields['terms'].label = "ACCEPT TERMS AND CONDITIONS"


class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()

	class Meta:
		model=User
		fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model=Profile
		fields=['image']


class AuthenticationFormWithChekUsersStatus(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if user.profile.status==False:
            raise forms.ValidationError(
                ({'username':"Your account has been blocked."}),
                code='inactive',
            )
