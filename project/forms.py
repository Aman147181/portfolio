from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    comment_body=forms.CharField(widget=forms.Textarea(attrs={'class': 'px-0 w-full text-sm text-gray-900 border-0 focus:ring-0 focus:outline-none dark:text-white dark:placeholder-gray-400 dark:bg-gray-800'}))

    class Meta:
        model = Comment
        fields = ('comment_body',)
