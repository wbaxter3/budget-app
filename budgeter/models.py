from django.db import models
from django.utils import timezone
import datetime


class UserAccount(models.Model):
    user_name = models.CharField(max_length=100,unique=True)
    monthly_income = models.FloatField()
    monthly_expenses = models.FloatField()

# budget model
class Budget(models.Model):

    budget_name = models.CharField(max_length=100, unique=True)
    max_amount = models.FloatField()
    current_amount = models.FloatField()
    userAccount = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    def __str__(self):
        return self.budget_name
