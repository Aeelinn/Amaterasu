from django.db import models


class NullCharField(models.CharField):
    description = "Charfield that stores NULL but returns ''"
    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        if isinstance(value, models.CharField):
            return value
        return value or ''

    def get_prep_value(self, value):
        return value or None