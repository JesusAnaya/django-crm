from django_crm.conf import settings


class DBField(object):
    tag_type = 'div'
    tag_id = ''
    tag_class = ''

    def content(self):
        return u''

    def render(self):
        tpl = '<{0} id="{1}" class="{2}">{3}</{0}>'
        content = self.content()
        return tpl.format(
            self.tag_type, self.tag_id, self.tag_class, content)


class SectionField(DBField):
    tag_type = 'section'
    tag_class = 'section'


class RowField(DBField):
    tag_type = 'section'
    tag_class = 'section'


class Dashboard(object):
    section_class = SectionField
    row_class = RowField

    def __init__(self):
        self.dashboard_schema = settings.DASHBOARD_SCHEMA

        self.section = self.section_class()
        self.row = self.row_class()
