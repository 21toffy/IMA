from django import forms
from .models import User
from django.core.exceptions import ValidationError

class UserCreationForm(forms.ModelForm):
    email = forms.CharField(label='email', widget=forms.EmailInput(attrs={'class':'form-control'}), max_length=30)
    firstname = forms.CharField(label='firstname', widget=forms.TextInput(attrs={'class':'form-control'}), max_length=30)
    lastname = forms.CharField(label='lastname', widget=forms.TextInput(attrs={'class':'form-control'}), max_length=30)
    mobile_number = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={'class':'form-control'}), max_length=11)
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'}), max_length=30)
    password2 = forms.CharField(label='repeat password', widget=forms.PasswordInput(attrs={'class':'form-control'}), max_length=30)

    # password = forms.CharField(widget=forms.PasswordInput())
    # password2 = forms.CharField(widget=forms.PasswordInput())
    

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get("password2")
        if p1 and p2:
            if p1 != p2:
                raise ValidationError('passwords do not match')
        return self.cleaned_data

    def clean_email(self):
        email= self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('This email has already Been used. ')
        return email

    def clean_mobile_number(self):
        mobile_number= self.cleaned_data['mobile_number']
        qs = User.objects.filter(mobile_number=mobile_number)
        if qs.exists():
            raise ValidationError('This mobile number has already Been used. ')
        return mobile_number 


    class Meta:
        model = User
        fields = ['mobile_number','email','firstname','lastname','password','password2']
        




class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100,)
   password = forms.CharField(widget=forms.PasswordInput())



# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     class Meta():
#         model = User
#         fields = ('username','password','email')
# class UserProfileInfoForm(forms.ModelForm):
#      class Meta():
#          model = UserProfileInfo
#          fields = ('portfolio_site','profile_pic')


#https://medium.com/@himanshuxd/how-to-create-registration-login-webapp-with-django-2-0-fd33dc7a6c67

#july 2017