from django.db import models
from django.utils import timezone
import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class UserMonthlyIncome(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    monthly_income = models.FloatField(default = 0)
# budget model
class Budget(models.Model):

    budget_name = models.CharField(max_length=100, unique=True)
    max_amount = models.FloatField()
    current_amount = models.FloatField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.budget_name
