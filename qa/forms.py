from django import forms

from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=512)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        _title = self.cleaned_data['title']
        _text = self.cleaned_data['text']
        qu = Question(title=_title, text=_text)
        return qu


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()

    def clean_question(self):
        qu_pk = self.cleaned_data['question']
        try:
            qu = Question.objects.get(pk=qu_pk)
        except:
            raise forms.ValidationError('question does not exist')
        else:
            return qu.pk

    def save(self):
        _text = self.cleaned_data['text']
        _question = self.cleaned_data['question']
        ask = Answer(text=_text, question_id=_question)
        return ask
