from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from taggit.forms import TagWidget
# Post creation/update form


# User registration
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# User update
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(attrs={'placeholder': 'Add tags separated by commas'})
        }


# Comment form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows':3, 'placeholder':'Add your comment'})
        }
