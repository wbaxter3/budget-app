from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Budget

class BudgetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['budget_name', 'max_amount', 'current_amount']})
    ]
admin.site.register(Budget, BudgetAdmin)
