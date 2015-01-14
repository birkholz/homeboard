from django.contrib.auth.models import User
from django.db import models
from home.models import AbstractTimestampModel, Home


class Message(AbstractTimestampModel):
    author = models.ForeignKey(User, related_name='messages')
    home = models.ForeignKey(Home, related_name='messages')

    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='message_images/', null=True, blank=True)

    def __unicode__(self):
        return '%s: %s on %s' % (self.home.title, self.author.username, self.created)

    class Meta:
        ordering = ['-created']
