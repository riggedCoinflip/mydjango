from django import forms

from users.models import User


class SettingsUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('about_text', 'github_name')
        labels = {
            'about_text': '',
            'github_name': ''
        }
        widgets = {
            'question_text': forms.TextInput(attrs={'placeholder': 'Describe yourself!'}),
            'github_name': forms.TextInput(attrs={'placeholder': 'Add your github username here'})
        }