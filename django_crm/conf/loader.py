from django.conf import settings as django_settings
from .models import Setting


class SettingsLoader(object):
    settings_queryset = Setting.objects.all()
    loaded_attrs = {}

    def __init__(self):
        self.loadconfig()

    def __getattr__(self, attribute):
        try:
            return self.loaded_attrs[attribute]
        except KeyError:
            return django_settings[attribute]

    def loadconfig(self):
        settings_attrs = {}

        for attribute in self.settings_queryset:
            settings_attrs[attribute.name] = attribute.value
        self.loaded_attrs = settings_attrs


#settings = SettingsLoader()
settings = django_settings
