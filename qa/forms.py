from django import forms
from django.forms import ModelForm

from .models import Question, Answer


class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']

    def save(self):
        _title = self.cleaned_data['title']
        _text = self.cleaned_data['text']
        qu = Question(title=_title, text=_text)
        qu.author_id = self._user
        qu.save()
        return qu


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']
        widgets = {'question': forms.HiddenInput()}

    def clean_question(self):
        _qu = self.cleaned_data['question']
        try:
            qu = Question.objects.get(pk=_qu.id)
        except:
            raise forms.ValidationError('question does not exist')
        else:
            return qu

    def save(self):
        _text = self.cleaned_data['text']
        _question = self.cleaned_data['question']
        ask = Answer(text=_text, question=_question)
        ask.author_id = self._user
        ask.save()
        return ask
