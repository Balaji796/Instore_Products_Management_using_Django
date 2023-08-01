from django import forms
class Stuform(forms.Form):
    name=forms.CharField(max_length=30)
    s_class=forms.CharField(max_length=30)
    addr=forms.CharField(max_length=30)
    school=forms.CharField(max_length=30)
    email=forms.CharField(max_length=30)
class Srchform(forms.Form):
    name=forms.CharField(max_length=30)
