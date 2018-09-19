from django import forms
from .models import Article,Author
class articleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title','content','author']