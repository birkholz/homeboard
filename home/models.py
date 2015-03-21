from django.contrib.auth.models import User
from django.db import models


class AbstractTimestampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Home(AbstractTimestampModel):
    title = models.CharField(max_length=50) # The name used in the url
    manager = models.ForeignKey(User, related_name='managed_homes')
    members = models.ManyToManyField(User, through='Member', related_name='homes')

    def __unicode__(self):
        return self.title


class Member(AbstractTimestampModel):
    user = models.ForeignKey(User)
    home = models.ForeignKey(Home)

    def __unicode__(self):
        return '%s in %s' % (self.user.username, self.home.title)