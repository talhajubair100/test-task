from distutils.log import error
from django.contrib.auth.models import Group
from allauth.account.forms import SignupForm, LoginForm
from django import forms
# from frontend.models import Profile


class CustomeSignupForm(SignupForm):
    def _init_(self, *args, **kwargs):
        super(CustomeSignupForm, self)._init_(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
        })
        

        

    def save(self, request):
        user = super(CustomeSignupForm, self).save(request)
        
           
        # group = Group.objects.get(name="client")
        # user.groups.add(group)
        
        # practitioner_user = Profile.objects.get_or_create(user=user)
       
        return user


class CustomeLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomeLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'type': 'email', 'placeholder': 'Email address', 'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})


