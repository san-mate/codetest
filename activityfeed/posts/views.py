# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from .models import FeedItem


class Posts(ListView):
    template_name = "list.html"
    model = FeedItem

    def get_queryset(self):
        return FeedItem.objects.all()


class MyPosts(ListView):
    template_name = "list.html"
    model = FeedItem

    def get_queryset(self):
        return FeedItem.objects.filter(user=self.request.user)


class FollowedPosts(ListView):
    template_name = "list.html"
    model = FeedItem

    def get_queryset(self):
        return FeedItem.objects.filter(user__registered_user__in=self.request.user.registered_user.tracking.all())
