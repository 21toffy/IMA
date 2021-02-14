from django import forms
from blog.models import *





class Blog_form(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class':'form-control'}), max_length=30)

    
    text = forms.CharField(label='text', widget=forms.TextInput(attrs={'class':'form-control'}), max_length=30)

    landing_image = forms.FileField(label='landing_image', widget=forms.ClearableFileInput(attrs={'class':'form-control'}))

    img2 = forms.FileField(label='image2', widget=forms.ClearableFileInput(attrs={'class':'form-control'}))

    img3 = forms.FileField(label='image3', widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    img4 = forms.FileField(label='image4', widget=forms.ClearableFileInput(attrs={'class':'form-control'}))

    img5 = forms.FileField(label='image5', widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    img6 = forms.FileField(label='image6', widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    vid = forms.FileField(label='video', widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    status = forms.ChoiceField(label='status', widget=forms.Select(choices=STATUS, attrs={'class':'form-control'}))

    category = forms.ChoiceField(label='category', widget=forms.Select(choices=CATEGORY, attrs={'class':'form-control'}))
    class Meta:
        model = Blog
        fields = ['title','text','landing_image','img2','img3','img4','img5','img6','vid','status','category']




class Edit_Blog_form(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class':'form-control'}), max_length=30)

    
    text = forms.CharField(label='text', widget=forms.TextInput(attrs={'class':'form-control'}), max_length=30)

    landing_image = forms.CharField(label='landing_image', widget=forms.Textarea(attrs={'class':'form-control', 'required': True}))

    img2 = forms.CharField(label='image2', widget=forms.TextInput(attrs={'class':'form-control', 'required': True}), max_length=30)

    img3 = forms.CharField(label='image3', widget=forms.Textarea(attrs={'class':'form-control', 'required': True}))
    img4 = forms.CharField(label='image4', widget=forms.TextInput(attrs={'class':'form-control', 'required': True}), max_length=30)

    img5 = forms.CharField(label='image5', widget=forms.Textarea(attrs={'class':'form-control', 'required': True}))
    img6 = forms.CharField(label='image6', widget=forms.Textarea(attrs={'class':'form-control', 'required': True}))
    vid = forms.CharField(label='video', widget=forms.Textarea(attrs={'class':'form-control'}))
    status = forms.CharField(label='status', widget=forms.Textarea(attrs={'class':'form-control'}))

    category = forms.CharField(label='category', widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Blog
        fields = ['title','text','landing_image','img2','img3','img4','img5','img6','vid','status','category']