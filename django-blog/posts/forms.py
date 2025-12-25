from django import forms
from .models import Feedback


class ShareArticleForm(forms.Form):
    """Form for sharing articles via email"""
    
    sender_name = forms.CharField(
        max_length=25,
        label="Ваше ім'я",
        widget=forms.TextInput(attrs={'placeholder': 'Введіть ваше ім\'я'})
    )
    sender_email = forms.EmailField(
        label='Ваш email',
        widget=forms.EmailInput(attrs={'placeholder': 'your@email.com'})
    )
    recipient_email = forms.EmailField(
        label='Email отримувача',
        widget=forms.EmailInput(attrs={'placeholder': 'recipient@email.com'})
    )
    message = forms.CharField(
        required=False,
        label='Повідомлення',
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Додайте своє повідомлення (необов\'язково)'
        })
    )


class FeedbackForm(forms.ModelForm):
    """Form for submitting feedback/comments"""
    
    class Meta:
        model = Feedback
        fields = ['author_name', 'author_email', 'content']
        labels = {
            'author_name': "Ваше ім'я",
            'author_email': 'Ваш email',
            'content': 'Коментар'
        }
        widgets = {
            'author_name': forms.TextInput(attrs={'placeholder': 'Введіть ім\'я'}),
            'author_email': forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'content': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Напишіть ваш коментар...'
            })
        }


class ArticleSearchForm(forms.Form):
    """Form for searching articles"""
    
    search_query = forms.CharField(
        label='Пошук',
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введіть запит для пошуку...'
        })
    )