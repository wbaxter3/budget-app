from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Budget
#from django.template import Context, Template
from django.contrib.auth.decorators import login_required
from .forms import *
import logging
import json
logger = logging.getLogger(__name__)


def index(request):
    all_budgets = Budget.objects.all()
    all_budgets_values = all_budgets.values()

    budgetDict = {}

    for budget in all_budgets_values:
        budgetDict[budget['id']] = {
            'budget_id': budget['id'],
            'budget_name': budget['budget_name'],
            'max_amount': budget['max_amount'],
            'current_amount':budget['current_amount']
        }
    print(budgetDict)
    return render(request, 'home.html', {'budgetDict':budgetDict})

@login_required
def create_new_budget(request):
    #if POST request process form data
    if request.method == 'POST':
        form = BudgetForm(request.POST)

        if form.is_valid():
            budget = Budget()
            budget.budget_name = request.POST.get('budget_name')
            budget.max_amount = request.POST.get('max_amount')
            budget.current_amount = 0
            budget.save()
            return redirect('home')

    else:
        form = BudgetForm()

    return render(request, 'create_budget.html', {'form': form})

# adds to current amount
@login_required
def add_to_current_amount(request, budget_id= None):

    if budget_id is None:
        form = AddToAmount(request.POST)

        if form.is_valid():
            budget = Budget
            budget = Budget.objects.get(pk=request.POST.get('budget_id'))
            budget.current_amount += int(request.POST.get('amount_to_add'))
            budget.save()
            return redirect('home')


    else:

        data_dict = {'budget_id': budget_id}
        form = AddToAmount(data_dict)
    return render(request, 'add_to_current_amount.html', {'form': form})

#
@login_required
def budget_success(request):
    # if request.method == 'POST':
    #     form = BudgetForm(reuqest.post)
    #     info = {
    #         'budget_name': form.cleaned_data['budget_name'],
    #         'max_amount': form.cleaned_data['max_amount']
    #     }
    return render(request, 'budget_success.html')
