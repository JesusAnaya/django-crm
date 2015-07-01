from django.contrib.sites.shortcuts import get_current_site
from django_crm.core.request import current_request


def get_current_site_id():
    request = current_request()
    site = get_current_site(request)
    site_id = getattr(site, 'id', None)
    return site_id
