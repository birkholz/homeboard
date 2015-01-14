from django.contrib.auth.models import User
from django.db import models
from home.models import AbstractTimestampModel, Home


class Bill(AbstractTimestampModel):
    home = models.ForeignKey(Home, related_name='bills')
    author = models.ForeignKey(User, related_name='authored_bills')

    amount = models.DecimalField(max_digits=8, decimal_places=2)
