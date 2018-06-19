# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import FeedItem, RegisteredUser


admin.site.register(FeedItem)
admin.site.register(RegisteredUser)
