from django import forms

class SampleForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    # can set initalize function


class SampleForm2(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    # set inital method
    def __init__(self, *args, **kwargs):

        # initial_name = 't'
        print(*args)
        super().__init__(*args, **kwargs)
        self.fields['name'].initial =  'override'


