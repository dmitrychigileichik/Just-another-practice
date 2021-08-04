from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Title', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='News text', required=False, widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "rows": 5
        }))
    is_published = forms.BooleanField(label='Published?', initial=True)
    category = forms.ModelChoiceField(empty_label='Choose category', queryset=Category.objects.all(), label='Category', widget=forms.Select(attrs={"class": "form-control"}))
