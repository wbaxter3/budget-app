from django.forms import ModelForm
from django import forms

class BudgetForm(forms.Form):

    budget_name = forms.CharField(label='budget name', max_length=100)
    max_amount = forms.IntegerField(label='max amount', min_value=0)

class AddToAmount(forms.Form):
    amount_to_add = forms.IntegerField(label='Amount spent since last update', min_value=0)
    budget_id = forms.IntegerField(widget=forms.HiddenInput())
