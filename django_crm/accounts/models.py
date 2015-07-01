from django.db import models
from django.core.urlresolvers import reverse
from django_crm.core.models import BaseModel, DataContact, AddressInformation
from django_crm.conf import settings


class AccountAbstract(BaseModel, DataContact, AddressInformation):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='accounts/', null=True, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('account-detail', kwargs={'pk': self.pk})


class Account(AccountAbstract):
    pass
