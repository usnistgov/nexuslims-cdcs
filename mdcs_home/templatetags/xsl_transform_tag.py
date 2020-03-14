"""XSL Transformation tag
"""

from django import template
from django.contrib.staticfiles import finders

from core_main_app.commons import exceptions
from core_main_app.components.template_xsl_rendering import api as template_xsl_rendering_api
from core_main_app.settings import DEFAULT_DATA_RENDERING_XSLT
from core_main_app.utils.file import read_file_content
# from core_main_app.utils.xml import xsl_transform
from mdcs_home.utils.xml import xsl_transform

register = template.Library()


class XSLType(object):
    type_list = "List"
    type_detail = "Detail"


@register.simple_tag(name='xsl_transform_list')
def render_xml_as_html(*args, **kwargs):
    """ Render an XML to HTML using the list xslt.
    Args:
        *args:
        **kwargs:
            ``xml_content``, ``template_id``, and ``template_hash`` will be 
            explicity parsed. Other kwargs will be passed to the XSLT object as
            parameters

    Returns:
        HTML

    """
    # import web_pdb; web_pdb.set_trace(port=3000)

    xml_content = kwargs.pop('xml_content')
    template_id = kwargs.pop('template_id', None)
    template_hash = kwargs.pop('template_hash', None)
    detail_url = '"{}"'.format(kwargs.pop('detail_url', '#'))
    return _render_xml_as_html(xml_content, template_id, template_hash, XSLType.type_list, detail_url=detail_url)


@register.simple_tag(name='xsl_transform_detail')
def render_xml_as_html(*args, **kwargs):
    """ Render an XML to HTML using the detail xslt.
    Args:
        *args:
        **kwargs:

    Returns:
        HTML

    """
    xml_content = kwargs.pop('xml_content')
    template_id = kwargs.pop('template_id', None)
    template_hash = kwargs.pop('template_hash', None)
    xmlName = '"{}"'.format(kwargs.pop('xmlName', ''))
    return _render_xml_as_html(xml_content, template_id, template_hash, XSLType.type_detail, xmlName=xmlName, **kwargs)


def _render_xml_as_html(xml_string, template_id=None, template_hash=None, xslt_type=XSLType.type_list, **kwargs):
    """ Render an XML to HTML according to an xslt type (list or detail).
    Args:
        xml_string:
        template_id:
        template_hash:
        xslt_type:
        kwargs: dict
            Other keyword arguments are passed to the XSLT object as parameters

    Returns:
        HTML

    """
    try:
        try:
            if template_id:
                template_xsl_rendering = template_xsl_rendering_api.get_by_template_id(template_id)
            elif template_hash:
                template_xsl_rendering = template_xsl_rendering_api.get_by_template_hash(template_hash)
            else:
                raise Exception("No template information provided. Default xslt will be used.")

            if xslt_type == XSLType.type_list:
                xslt_string = template_xsl_rendering.list_xslt.content
            elif xslt_type == XSLType.type_detail:
                xslt_string = template_xsl_rendering.detail_xslt.content
            else:
                raise Exception("XSLT Type unknown. Default xslt will be used.")
        except (Exception, exceptions.DoesNotExist):
            default_xslt_path = finders.find(DEFAULT_DATA_RENDERING_XSLT)
            xslt_string = read_file_content(default_xslt_path)

        return xsl_transform(xml_string, xslt_string, **kwargs)
    except Exception:
        return xml_string
