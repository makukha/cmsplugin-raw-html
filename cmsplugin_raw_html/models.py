from cms.models import CMSPlugin
from django.db import models


class RawHtmlPlugin(CMSPlugin):

    body = models.TextField('HTML')

    def __unicode__(self):
        return str(self.body)
