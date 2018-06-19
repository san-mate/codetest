# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Ownable(models.Model):
    user = models.ForeignKey('auth.User', verbose_name=_('Author'),
                             related_name='%(class)ss')
    class Meta:
        abstract = True


class RegisteredUser(models.Model):
    user = models.OneToOneField(User, related_name='registered_user')
    tracking = models.ManyToManyField('self', related_name='tracked_by',
                                      blank=True, symmetrical=False)

    def __unicode__(self):
        return "%s" % self.user


class FeedItem(Ownable):
    content = models.CharField('Content', max_length=1000, blank=True, null=True)

    def __unicode__(self):
        return "%s" % self.content
