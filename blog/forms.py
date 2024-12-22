import django.forms as forms
from .models import Blog, ContactFormResponse, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }
        
        
class ContactFormResponseForm(forms.ModelForm):
    class Meta:
        model = ContactFormResponse
        fields = ['name', 'email', 'subject', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control w-50'}),
        }
