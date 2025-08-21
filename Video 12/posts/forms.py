from django import forms 
from .models import *


class BlogForm(forms.ModelForm): 
    title = forms.CharField(
        label="Blog post title",
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the title of your blog post...'
        })
    )
    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(attrs={
            'placeholder': 'Write your blog post here...',
            'rows':8,
        })
    )

    image = forms.ImageField(
        label = 'Upload an image',
        required=False,
        widget= forms.ClearableFileInput()
    )

    class Meta: 
        model= BlogPost
        fields= ['title', 'content','image']