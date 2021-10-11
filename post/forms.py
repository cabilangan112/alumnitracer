from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)
        fields = ('user',
 
        'banner_photo',
        'body',
        'status',
        )
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': "What's on your mind ? "   }),
        }
 
 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post','author',)
        fields = (
        'post',
        'text',
        'author',)
    
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': "Write a comment..."   }),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)
        fields = ('user',
 
        'banner_photo',
        'body',
        'status',)