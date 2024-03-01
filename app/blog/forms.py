from django import forms
from .models import Review
from django.core.exceptions import ValidationError


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'text', 'images', 'category', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'text': forms.Textarea(attrs={'placeholder': 'Text'}),
            'images': forms.FileInput(attrs={'placeholder': ''}),
            'category': forms.Select(attrs={'class': ''}),
            'is_published': forms.CheckboxInput(attrs={'class': ''}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError("Your title can't be longer than 50 symbols")
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 20:
            raise ValidationError("Your text can't be less than 20 symbols")
        return text

