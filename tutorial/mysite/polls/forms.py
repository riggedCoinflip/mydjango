from django import forms
from django.forms.models import inlineformset_factory

from .models import Question, Choice

questionFormSize = 50

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',)
        labels = {
            'question_text': ''
        }
        widgets = {
            'question_text': forms.TextInput(attrs={'placeholder': 'Enter Question here', 'size': questionFormSize})
        }

class ChoiceInline(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('choice_text',)
        labels = {
            'choice_text': ''
        }
        widgets = {
            'choice_text': forms.TextInput(attrs={'placeholder': 'Enter Choice here', 'size': questionFormSize})
        }


QuestionInlineFormSet = inlineformset_factory(
    Question, Choice, form=ChoiceInline, min_num=2, max_num=10, extra=0, can_delete=False,
)
