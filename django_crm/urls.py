from django.conf.urls import include, url

urlpatterns = [
    url(r'^account/', include('django_crm.accounts.urls')),
]
