from django.db import models
from django.utils import timezone
import datetime
from django.db import models

# budget model
class Budget(models.Model):

    budget_name = models.CharField(max_length=100)
    max_amount = models.FloatField()
    current_amount = models.FloatField()

    def __str__(self):
        return self.budget_name
