from django.contrib.auth.models import User
from django.db import models
from home.models import AbstractTimestampModel, Home


class Chore(AbstractTimestampModel):
    home = models.ForeignKey(Home, related_name='chores')
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ManyToManyField(User, through='Assignment')

    def __unicode__(self):
        return '%s: %s' % (self.home.title, self.title)

    class Meta:
        ordering = ['-created']


class Assignment(AbstractTimestampModel):
    user = models.ForeignKey(User)
    chore = models.ForeignKey(Chore)


