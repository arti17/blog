from django import forms

from webapp.models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['created_at', 'updated_at']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['created_at', 'updated_at']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=60, required=False, label='Search')
