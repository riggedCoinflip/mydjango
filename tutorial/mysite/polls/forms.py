from django import forms
from django.forms.models import inlineformset_factory

from .models import Question, Choice


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']


class ChoiceInline(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']


QuestionInlineFormSet = inlineformset_factory(
    Question, Choice, form=ChoiceInline, min_num=2, max_num=10, extra=0, can_delete=False
)


