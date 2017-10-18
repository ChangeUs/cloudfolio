from django.db import models


class TimeStampedModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FormatOfPeriodModel(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        abstract = True


class PrivacyModel(models.Model):

    # Model constants #

    PRIVATE = 0
    PUBLIC_ALL = 1

    # Attributes of Privacy model

    privacy = models.IntegerField(default=PUBLIC_ALL)

    # Meta information

    class Meta:
        abstract = True
