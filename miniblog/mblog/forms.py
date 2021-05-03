from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from .models import blogPost, Contact

# for signup

class signupForm(UserCreationForm):
    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = 'Confirm password(again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {

        'username' : forms.TextInput(attrs={'class':'form-control'}),
        'first_name' : forms.TextInput(attrs={'class':'form-control'}),
        'last_name' : forms.TextInput(attrs={'class':'form-control'}),
        'email' : forms.EmailInput(attrs={'class':'form-control'}),

        }

 # for login
class loginForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class': 'form-control'}))
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class': 'form-control'}))



class PostForm(forms.ModelForm):
    class Meta:
        model = blogPost
        fields = ['title', 'desc']
        labels = {'title':'Title', 'desc':'Description'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'}),

        }
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'}),
        }        