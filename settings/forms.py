from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Row, Column, ButtonHolder, Submit
from django import forms
from users.models import User


class SettingsUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('avatar', 'about_text', 'github_name')
        labels = {
            'avatar': '',
            'about_text': '',
            'github_name': ''  # label moved to Layout to allow for hacky inline solution
        }
        widgets = {
            'about_text': forms.Textarea(attrs={'placeholder': 'Describe yourself!💯'}),
            'github_name': forms.TextInput(attrs={'class': 'form-inline',
                                                  'placeholder': 'your_github_name'}),
        }
        help_texts = {
            'github_name': 'You may showcase a project as well: <em>/username/fav_project</em>',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)  # this is required to display the help_texts
        '''
        hacky solution - replace the standard label with a fake label. 
        Wrap those 2 as columns of a Row - use col-auto on first to not have whitespace between.
        Use g-0 to not have gutters between columns - padding and margin would else create whitespace
        '''
        self.helper.layout = Layout(
            Div('avatar'),
            Div('about_text'),
            Row(
                # create a "fake" label with a HTML Column
                Column(HTML('<em class="fab fa-github fa-2x"></em> github.com/'), css_class='col-auto'),
                Column('github_name', css_class='col'),
                css_class='row g-0'
            ),
            ButtonHolder(
                Submit('submit', 'Save', css_class='btn btn-success')
            )
        )

    def clean_github_name(self):
        github_name = self.cleaned_data['github_name']
        github_name = github_name.strip(' /')
        return github_name
