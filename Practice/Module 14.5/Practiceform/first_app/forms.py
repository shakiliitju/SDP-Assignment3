from django import forms

class ExampleForm(forms.Form):

	email = forms.EmailField()
