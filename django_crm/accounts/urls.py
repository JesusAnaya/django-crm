from django.conf.urls import url
from django_crm.accounts import views

urlpatterns = [
    url(r'^$', views.AccountList.as_view(), name='account-list'),
    url(r'^(?P<pk>\w+)/$', views.AccountDetail.as_view(), name='account-detail'),
]
