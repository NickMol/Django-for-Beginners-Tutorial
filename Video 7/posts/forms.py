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
        widget=forms.TextInput(attrs={
            'placeholder': 'Write your blog post here...'
        })
    )

    class Meta: 
        model= BlogPost
        fields= ['title', 'content']