# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

ROBOT_TAGS = (
    ('index,follow', 'Index, Follow'),
    ('noindex,follow', 'No index, Follow'),
    ('index,nofollow', 'Index, No follow'),
    ('noindex,nofollow', 'No index, No follow'),
)


class Document(models.Model):
    """
    Meta-information for document.
    """
    url = models.CharField(_('URL'), max_length=255)
    title = models.CharField(_('Title'), max_length=140)
    description = models.TextField(_('Description'), blank=True, null=True)
    keywords = models.CharField(
        _('Keywords'),
        max_length=255,
        blank=True,
        null=True,
    )
    robot_tags = models.CharField(
        _('Robots'),
        max_length=20,
        choices=ROBOT_TAGS,
        default=ROBOT_TAGS[0][0],
    )

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')
        ordering = ('url', )

    def __unicode__(self):
        return self.title
