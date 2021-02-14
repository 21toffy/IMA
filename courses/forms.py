from django import forms
from django.forms import TextInput
from .models import UserCourse, Course


class UserCourseForm(forms.ModelForm):
        
    widgets = {
        'user': TextInput(attrs={'readonly': 'readonly'})
    }

    # user = forms.CharField(label='user', widget=forms.TextInput(attrs={'class':'form-control', }), max_length=30)

    # course = forms.CharField(label='course', widget=forms.TextInput(attrs={'class':'form-control', }), max_length=30)

    class Meta:
        model =UserCourse
        fields = ['user', 'course']


class CourseForm(forms.ModelForm):
    class Meta:
        model =  Course
        fields = ['name', 'price']
        widgets = {
            'name': TextInput(attrs={'readonly': 'readonly'}),
            'price': TextInput(attrs={'readonly': 'readonly'})
        }

