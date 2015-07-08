from django.conf import settings as django_settings
from django_crm.conf import settings_crm


class SettingsLoader(object):
    #settings_queryset = Setting.objects.all()
    loaded_attrs = {}

    def __init__(self):
        pass
        #self.loadconfig()

    def __getattr__(self, attribute):
        attr = getattr(django_settings, attribute)
        if attr in None:
            attr = getattr(settings_crm, attribute)
        return attr

    # def loadconfig(self):
    #     settings_attrs = {}

    #     for attribute in self.settings_queryset:
    #         settings_attrs[attribute.name] = attribute.value
    #     self.loaded_attrs = settings_attrs


settings = SettingsLoader()
#settings = django_settings
