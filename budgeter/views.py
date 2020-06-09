from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import *
#from django.template import Context, Template
from django.contrib.auth.decorators import login_required
from .forms import *
import logging
import json
logger = logging.getLogger(__name__)


def index(request):
    if request.user.is_authenticated:
        all_budgets = Budget.objects.filter(user=request.user)
        all_budgets_values = all_budgets.values()

        budgetDict = {}
        monthly_expenses = 0
        for budget in all_budgets_values:
            budgetDict[budget['id']] = {
                'budget_id': budget['id'],
                'budget_name': budget['budget_name'],
                'max_amount': budget['max_amount'],
                'current_amount':budget['current_amount'],
                'amount_left':budget['max_amount']-budget['current_amount']

            }
            monthly_expenses += float(budget['max_amount']-budget['current_amount'])
        user_monthly_income = UserMonthlyIncome.objects.filter(user=request.user)
        user_values = user_monthly_income.values()
        user_dict = {}
        if user_values.count() != 0:

            user_dict['monthly_income'] = user_values[0]['monthly_income']
            user_dict['monthly_expenses'] = monthly_expenses
            user_dict['left_over'] = user_values[0]['monthly_income'] - monthly_expenses

    else:
        budgetDict = user_dict = {}

    return render(request, 'home.html', {'budgetDict':budgetDict, "user_dict":user_dict})

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
            budget.user = request.user
            budget.save()
            return redirect('home')

    else:
        form = BudgetForm()

    return render(request, 'create_budget.html', {'form': form})


@login_required
def delete_budget(request):
    #if POST request process form data
    budget_id = int(request.POST.get('budget_id'))
    budget = Budget.objects.get(pk=budget_id)
    budget.delete()


    return redirect('home')

# adds to current amount
@login_required
def add_to_current_amount(request, budget_id= None):

    if budget_id is None:
        form = AddToAmount(request.POST)

        if form.is_valid():
            budget = Budget.objects.get(pk=request.POST.get('budget_id'))
            budget.current_amount += float(request.POST.get('amount_to_add'))
            budget.save()
            return redirect('home')


    else:

        data_dict = {'budget_id': budget_id}
        form = AddToAmount(data_dict)
    return render(request, 'add_to_current_amount.html', {'form': form})


@login_required
def edit_budget(request, budget_id=None):

    if budget_id:
        budget = Budget.objects.get(pk=budget_id)
        data_dict = {
            'budget_id': budget_id,
            'budget_name': budget.budget_name,
            'max_amount': budget.max_amount,
            'current_amount': budget.current_amount
        }
        form = EditBudget(initial=data_dict)
        return render(request, 'edit_budget.html', {'form':form})

    else:
        form = EditBudget(request.POST)
        if form.is_valid():
            budget = Budget.objects.get(pk=request.POST.get('budget_id'))
            budget.budget_name = request.POST.get('budget_name')
            budget.max_amount = request.POST.get('max_amount')
            budget.current_amount = request.POST.get('current_amount')
            budget.save()
            return redirect('home')


@login_required
def edit_monthly_income(request):

    if request.method=='GET':
        user_monthly_income = UserMonthlyIncome.objects.get(user=request.user)
        data_dict = {
            'monthly_income': user_monthly_income.monthly_income
        }
        form = EditMonthlyIncome(initial=data_dict)
        return render(request, 'edit_monthly_income.html', {'form':form})

    else:
        form = EditMonthlyIncome(request.POST)
        if form.is_valid():
            user_monthly_income = UserMonthlyIncome.objects.get(user=request.user)
            user_monthly_income.monthly = request.POST.get('monthly_income')
            user_monthly_income.save()
            return redirect('home')

@login_required
def create_new_monthly_income(request):

    if request.method=='GET':

        form = EditMonthlyIncome()
        return render(request, 'create_new_monthly_income.html', {'form':form})

    else:

        form = EditMonthlyIncome(request.POST)
        if form.is_valid():
            user_monthly_income = UserMonthlyIncome()
            user_monthly_income.user = request.user
            user_monthly_income.monthly_income = request.POST.get('monthly_income')
            user_monthly_income.save()
            return redirect('home')

@login_required
def reset_budget(request):
    all_budgets = Budget.objects.filter(user=request.user)
    all_budgets_values = all_budgets.values()
    for budget in all_budgets_values:
        budget = Budget.objects.get(pk=budget['id'])
        budget.current_amount = 0
        budget.save()
    return redirect('home')
