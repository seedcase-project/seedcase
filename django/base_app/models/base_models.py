"""
This file contains the base app defaul base django model
-------------------------------------------------------------------------------
"""


from django.db import models
from django.db.utils import IntegrityError
from django.contrib.auth.models import User


class BaseManager(models.Manager):
    """
    The purpose to overriding normal Manager behaviour is to support
    case-insensitive matching.
    """

    def get(self, *args, **kwargs):
        return super(BaseManager, self).get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        return super(BaseManager, self).filter(*args, **kwargs)


class BaseModel(models.Model):
    """
    Defines an abstract model built off of Django's Model class that
    provides some common fields that are useful across the application.
    """

    objects = BaseManager()

    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True, null=True)
    last_modified_by = models.ForeignKey(
        User,
        related_name="%(app_label)s_%(class)s_related",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def save(self, *args, **kwargs):
        try:
            for unique_set in type(self)._meta.unique_together:
                for attr in unique_set:
                    get_args = {}
                    get_args[attr] = getattr(self, attr, None)
                self._check_db_for_duplicate(get_args)
        except TypeError:
            pass

        return super(BaseModel, self).save(*args, **kwargs)

    def _check_db_for_duplicate(self, kwargs):
        if len(kwargs) == 0:
            return
        try:
            result = type(self).objects.filter(**kwargs).exclude(id=self.id)
            if len(result) > 0:
                raise IntegrityError("Entry already exists %s" % str(kwargs))
        except self.DoesNotExist:
            pass

    class Meta:
        abstract = True


class Address(models.Model):
    """
    Relatively standard address model.
    Designed to be subclassed with multiple inheritance by any model
    requiring an address.
    """

    address = models.CharField(
        max_length=128, null=True, blank=True, verbose_name="Address line 1"
    )
    address2 = models.CharField(
        max_length=128, null=True, blank=True, verbose_name="Address line 2"
    )
    city = models.CharField(max_length=32, null=True, blank=True)
    province = models.CharField(
        max_length=32, null=True, blank=True, help_text="Full province name"
    )
    postal_code = models.CharField(max_length=16, null=True, blank=True)
    country = models.CharField(
        max_length=2,
        null=True,
        blank=True,
        help_text="ISO two-letter country code",
    )

    class Meta:
        abstract = True
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.get_full_address()

    def get_full_address(self):
        """
        Return a text list of address fields present in the object, by line.
        """
        fields_to_display = list()
        if self.address:
            fields_to_display.append(self.address)
        if self.address2:
            fields_to_display.append(self.address2)
        if self.city and self.province:
            fields_to_display.append("%s, %s" % (self.city, self.province))
        elif self.city:
            fields_to_display.append(self.city)
        elif self.province:
            fields_to_display.append(self.province)
        if self.country:
            fields_to_display.append(self.country)
        if self.postal_code:
            fields_to_display.append(self.postal_code)
        return "\n".join(fields_to_display)
