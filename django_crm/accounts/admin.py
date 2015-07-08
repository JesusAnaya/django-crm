from django.contrib import admin
from django_crm.core.admin import BaseAdmin
from django_crm.accounts.models import Account


class AccountAdmin(BaseAdmin):
    fieldsets = (
        ('Account Information', {
            'fields': ('name', 'owner', 'image', 'email', 'phone', 'fax', 'website')
        }),
        ('Address Information', {
            'fields': (
                'billing_street',
                'billing_state',
                'billing_city',
                'billing_zip_code',
                'billing_country',
                'shiping_street',
                'shiping_state',
                'shiping_city',
                'shiping_zip_code',
                'shiping_country',
            )
        }),
    )


admin.site.register(Account, AccountAdmin)
