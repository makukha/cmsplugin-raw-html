from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.template import Template
from django.utils.safestring import mark_safe

from cmsplugin_raw_html.models import RawHtmlPlugin


class CMSRawHtmlPlugin(CMSPluginBase):

    model = RawHtmlPlugin
    name = 'HTML'
    render_template = 'cmsplugin_raw_html/raw.html'
    text_enabled = True

    def render(self, context, instance, placeholder):
        context.update({
            'body': mark_safe(Template(instance.body).render(context)),
            'object': instance,
            'placeholder': placeholder
            })
        return context

plugin_pool.register_plugin(CMSRawHtmlPlugin)
