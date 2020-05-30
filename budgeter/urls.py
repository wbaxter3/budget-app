"""budgeter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='home'),
    path('create_new_budget/', views.create_new_budget, name='create_budgets'),
    path('budget_success/', views.budget_success, name='budget_success'),
    path('add_to_current_amount/', views.add_to_current_amount, name='add_to_current_amount'),
    path('add_to_current_amount/<int:budget_id>/', views.add_to_current_amount, name='add_to_current_amount')
]


# in the middle of updating the add to current amount form
