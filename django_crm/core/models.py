from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.sites.managers import CurrentSiteManager
from django_crm.utils.sites import get_current_site_id


class SiteRelated(models.Model):
    """
    Abstract model for all things site-related. Adds a foreignkey to
    Django's ``Site`` model.
    """

    objects = CurrentSiteManager()

    class Meta:
        abstract = True

    site = models.ForeignKey("sites.Site", editable=False)

    def save(self, update_site=False, *args, **kwargs):
        """
        Set the site to the current site when the record is first
        created, or the ``update_site`` argument is explicitly set
        to ``True``.
        """
        if update_site or (self.id is None and self.site_id is None):
            self.site_id = get_current_site_id()
        super(SiteRelated, self).save(*args, **kwargs)


class BaseModel(SiteRelated):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DataContact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    fax = models.CharField(max_length=30)
    website = models.URLField(max_length=300)

    class Meta:
        abstract = True


class AddressInformation(models.Model):
    billing_street = models.CharField(max_length=355)
    billing_state = models.CharField(max_length=255)
    billing_city = models.CharField(max_length=255)
    billing_zip_code = models.CharField(max_length=7)
    billing_country = models.CharField(max_length=255)

    shiping_street = models.CharField(max_length=355)
    shiping_state = models.CharField(max_length=255)
    shiping_city = models.CharField(max_length=255)
    shiping_zip_code = models.CharField(max_length=7)
    shiping_country = models.CharField(max_length=255)

    class Meta:
        abstract = True


class RelationShipModel(BaseModel):
    class Meta:
        abstract = True
