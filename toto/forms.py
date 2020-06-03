from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, Textarea
from .models import *

class NewUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title']
        labels = {
            'title': 'Question',
        }

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': 'Your Answer'
        }
        widgets = {
            'content': Textarea(attrs={'cols':80, 'rows':100, 'style':'height: 50vh;'}),
        }
