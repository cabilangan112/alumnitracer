from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)
        fields = ('user',
        'title',
        'banner_photo',
        'body',
        'status',)
 
 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('post','author',)
        fields = (
        'post',
        'text',
        'author',)
    
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)
        fields = ('user',
        'title',
        'banner_photo',
        'body',
        'status',)