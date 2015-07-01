from django.db import models
from django_crm.core.mixins import DataContactMixing
from django_crm.entity.models import EntityAbstract


class ContactAbstract(DataContactMixing, EntityAbstract):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='contacts/', null=True, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name()

    def name(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return ''


class Contact(ContactAbstract):
    pass
