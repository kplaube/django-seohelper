# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

from seohelper.models import Document, ROBOT_TAGS


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', )
    search_fields = ('title', 'description', )


admin.site.register(Document, DocumentAdmin)
