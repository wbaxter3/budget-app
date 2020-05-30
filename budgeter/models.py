from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
from django.db import models


class Budget(models.Model):

    budget_name = models.CharField(max_length=100)
    max_amount = models.IntegerField()
    current_amount = models.IntegerField()

    def __str__(self):
        return self.budget_name

    def setCurrentAmount(self, new_amount):

        self.current_amount = new_amount
