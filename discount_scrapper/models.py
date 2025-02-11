from django.conf import settings
from django.db import models
from django.utils import timezone

from helpers.models import TrackingModel


class Course(TrackingModel, models.Model):
    title = models.CharField(max_length=500)
    url = models.URLField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="User Details",
    )
    discount_active = models.BooleanField(default=False)
    last_recorded_discount_date = models.DateTimeField()
    meta_data = models.JSONField(
        default=dict, null=True, blank=True
    )
