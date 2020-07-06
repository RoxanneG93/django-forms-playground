from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Snippet


class NameWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        super().__init__([
            forms.TextInput(),
            forms.TextInput()
        ], attrs)
    
    def decompress(self, value):
        if value:
            return value.split(' ')
        return ['', '']
        # will return as ['firstValue'. 'secondValue']

class NameField(forms.MultiValueField):

    widget = NameWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(), #firstValue
            forms.CharField() #secondValue
        )

        super().__init__(fields, *args, **kwargs)

        # datalist takes each of the form feilds and puts it into a list
    def compress(self, data_list):
        # Example data_list = ['firstValue', 'secondValue']
        return f'{data_list[0]} {data_list[1]}'
        # this will return as 'firstValue secondValue'


class LargeForm(forms.Form):
    name = NameField()
    email = forms.EmailField(label='E-Mail')
    category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)

    # instatiating this form as a chrispy form 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'name',
            'email',
            'category',
            'subject',
            'body',
            Submit('submit', 'Submit', css_class='btn-sucess' )
        )


class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('name', 'body')