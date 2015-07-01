from django.views.generics import ViewBase


class EntityViewBase(ViewBase):
    def get_special_field_from_model(self):
        pass
