from django import forms
from django.core.exceptions import ValidationError
from webapp.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = {'author', 'text', 'email'}
        labels = {
            'author': 'Автор',
            'text': 'Текст',
            'email': 'Почта',
        }

    def clean_title(self):
        author = self.cleaned_data.get('author')
        if len(author) < 2:
            raise ValidationError('Имя автора должно быть длиннее двух символов!')
        return author
