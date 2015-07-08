from django.views.generic import ListView, DetailView
from django_crm.contacts.models import Contact


class ContactList(ListView):
    template_name = 'account/list.html'
    model = Contact
    context_object_name = 'accounts'


class ContactDetail(DetailView):
    template_name = 'account/profile.html'
    model = Contact
    context_object_name = 'account'
