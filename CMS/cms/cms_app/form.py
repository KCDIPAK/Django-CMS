from django.forms import ModelForm
from .models import *
from django import forms

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


class UserCreationFrom(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = '__all__'



