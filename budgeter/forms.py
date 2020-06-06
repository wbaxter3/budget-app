from django.forms import ModelForm
from django import forms

class BudgetForm(forms.Form):

    budget_name = forms.CharField(label='budget name', max_length=100)
    max_amount = forms.FloatField(label='max amount', min_value=0, widget=forms.NumberInput(attrs={'step':"0.01"}))

class AddToAmount(forms.Form):
    amount_to_add = forms.FloatField(label='Amount spent since last update', min_value=0,
    widget=forms.NumberInput(attrs={'step':"0.01"}))
    budget_id = forms.IntegerField(widget=forms.HiddenInput())

class EditBudget(forms.Form):
    budget_name = forms.CharField(label='budget name', max_length=100)
    max_amount = forms.FloatField(label='max amount', min_value=0,widget=forms.NumberInput(attrs={'step':"0.01"}))
    current_amount = forms.FloatField(label='current amount', min_value=0,widget=forms.NumberInput(attrs={'step':"0.01"}))
    budget_id = forms.IntegerField(widget=forms.HiddenInput())
