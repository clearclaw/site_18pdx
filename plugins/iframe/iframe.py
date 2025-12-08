# -*- coding: utf-8 -*-

"""
iframe directive for reStructuredText.

basic use in reST document:

.. iframe:: https://google.com/
    :width: 640
    :height: 480
"""

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from nikola.plugin_categories import RestExtension
from nikola.plugins.compile.rest import _align_choice, _align_options_base

CODE = """\
<iframe class="iframe-embed{align}" width="{width}" height="{height}"
 scrolling="no" frameborder="no"
 src="{src}">
</iframe>"""


class Plugin(RestExtension):
    """Plugin for iframe directive"""

    name = "rest_iframe"
    
    def set_site(self, site):
        """Set Nikola site."""
        self.site = site
        directives.register_directive('iframe', Iframe)
        return super().set_site(site)


class Iframe(Directive):
    """reST extension for adding an iframe"""

    has_content = True
    required_arguments = 1
    option_spec = {
        "width": directives.positive_int,
        "height": directives.positive_int,
        "align": _align_choice
    }


    def run(self):

        options = {
            "src": self.arguments[0],
            "width": 640,
            "height": 480,
        }
        options.update(self.options)

        if self.options.get("align") in _align_options_base:
            options["align"] = " align-" + self.options["align"]
        else:
            options["align"] = ''

        return [nodes.raw('', CODE.format(**options), format='html')]
