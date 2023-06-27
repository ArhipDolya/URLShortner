from django import forms


class FormUrl(forms.Form):

    url = forms.CharField(max_length=500)
    #unique_id = forms.CharField(max_length=20)