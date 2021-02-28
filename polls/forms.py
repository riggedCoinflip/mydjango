from django import forms

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


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('choice_text',)
        labels = {
            'choice_text': ''
        }
        widgets = {
            'choice_text': forms.TextInput(attrs={'placeholder': 'Enter Choice here', 'size': questionFormSize})
        }

