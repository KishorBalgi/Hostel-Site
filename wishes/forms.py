from django import forms
from .models import Wishes

class WishesForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 14,
        'minlength': 50,
        'title': "Your Message",
        'label': 'Your Message'

    }))
    class Meta:
        model = Wishes
        fields = ['name', 'batch', 'content']
        labels = {
            'name': 'Enter your full name',
            'batch': 'VKSSF Batch',
            'content': 'Your message'
        }

    def __init__(self, *args, **kwargs):
        super(WishesForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = 'Your Message'
