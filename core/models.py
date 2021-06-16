from django.db import models

# from django.db.models.base import Model
# from django.db.models.fields import DateTimeField

# Create your models here.


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
