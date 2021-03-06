from learning_app.models import UserProfileModel, Memory
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileModel
        fields = ('portfolio', 'profile_picture')

class MemoryForm(forms.ModelForm):

    class Meta:
        model = Memory
        fields = [ 'photo', 'desc']
        widgets = {
                'desc': forms.TextInput(attrs={'class': ''})
         }
