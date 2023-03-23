from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(label='With album title containing:', max_length=100)
    