from django import forms
from .models import Review
from django.core.exceptions import ValidationError


class AddReviewForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = "Select type"
        self.fields['category'].empty_label = "Select category"
        self.fields['tags'].empty_label = "Select tags"


    class Meta:
        model = Review
        fields = ['title', 'text', 'images', 'type', 'category', 'tags', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'text': forms.Textarea(attrs={'placeholder': 'Text'}),
            'images': forms.FileInput(),
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


