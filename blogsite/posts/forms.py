from django import forms
from .models import Feedback


class ShareArticleForm(forms.Form):
    """Form for sharing article via email"""
    
    sender_name = forms.CharField(
        max_length=100,
        label='Ваше ім\\'я',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введіть ваше ім\\'я'
        })
    )
    sender_email = forms.EmailField(
        label='Ваш email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your.email@example.com'
        })
    )
    recipient_email = forms.EmailField(
        label='Email одержувача',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'recipient@example.com'
        })
    )
    message = forms.CharField(
        required=False,
        label='Повідомлення',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Додайте особисте повідомлення (необов\\'язково)'
        }
        )
    )
    
    def clean_recipient_email(self):
        recipient = self.cleaned_data.get('recipient_email')
        sender = self.cleaned_data.get('sender_email')
        if recipient and sender and recipient == sender:
            raise forms.ValidationError('Не можна відправити статтю самому собі!')
        return recipient


class FeedbackForm(forms.ModelForm):
    """Form for submitting feedback/comments"""
    
    class Meta:
        model = Feedback
        fields = ['author_name', 'author_email', 'content']
        labels = {
            'author_name': 'Ваше ім\'я',
            'author_email': 'Ваш email',
            'content': 'Коментар'
        }
        widgets = {
            'author_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Як вас звати?'
            }),
            'author_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Напишіть ваш коментар тут...'
            })
        }
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if content and len(content) < 10:
            raise forms.ValidationError('Коментар занадто короткий. Мінімум 10 символів.')
        return content