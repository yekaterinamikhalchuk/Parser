from django.forms import ModelForm
from .models import News
from django import forms

class ParserForm(ModelForm):

    class Meta:
        model = News
        fields = ['update_date',
            'domain',
            'link',
            'create_date',
            'update_date',
            'country', 'is_dead']