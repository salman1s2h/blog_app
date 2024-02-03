from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from.models import User


class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User        
        fields = ("username", "email","birth_date","name")
        # fields = ("username",)

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)

        # user.user_type = self.cleaned_data['user_type']
        user.email = self.cleaned_data['email']
        user.birth_date = self.cleaned_data['birth_date']
        user.name = self.cleaned_data['name']

        if commit:
            user.save()

        return user
    
class LoginForm(forms.Form):

    email = forms.CharField()
    password = forms.CharField()