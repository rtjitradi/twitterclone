from django import forms


class AddTweetForm(forms.Form):
    characters = forms.CharField(max_length=140)
