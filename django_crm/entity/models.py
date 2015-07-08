from django.db import models
from django_crm.core.models import BaseModel
from django_crm.conf import settings


class EntityAbstract(BaseModel):
    name = models.CharField(max_length=255)
    account = models.ForeignKey(settings.ACCOUNT_MODEL)

    class Meta:
        abstract = True
