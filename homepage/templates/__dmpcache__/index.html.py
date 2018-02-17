# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1518849812.11027
_enable_loop = True
_template_filename = '/Users/victoriaashworth/Documents/Projects/randomuser/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        response = context.get('response', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(str( response ))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/victoriaashworth/Documents/Projects/randomuser/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"17": 0, "23": 1, "24": 1, "30": 24}}
__M_END_METADATA
"""
