from django.views.generic import ListView, DetailView
from django_crm.accounts.models import Account


class AccountList(ListView):
    template_name = 'account/list.html'
    model = Account
    context_object_name = 'accounts'


class AccountDetail(DetailView):
    template_name = 'account/profile.html'
    model = Account
    context_object_name = 'account'
