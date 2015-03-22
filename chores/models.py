from django.contrib.auth.models import User
from django.contrib.humanize.templatetags import humanize
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db import models
from django.utils import timezone
from home.models import AbstractTimestampModel, Home


class Chore(AbstractTimestampModel):
    home = models.ForeignKey(Home, related_name='chores')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assigned_to = models.ManyToManyField(User, through='Assignment')
    completed = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return '%s: %s' % (self.home.title, self.title)

    def pretty_completed(self):
        if self.completed:
            current_tz = timezone.get_current_timezone()
            adjusted = self.completed.astimezone(current_tz)
            return naturaltime(adjusted)
        return None

    class Meta:
        ordering = ['-created']


class Assignment(AbstractTimestampModel):
    user = models.ForeignKey(User)
    chore = models.ForeignKey(Chore)

    class Meta:
        unique_together = [('user', 'chore')]
