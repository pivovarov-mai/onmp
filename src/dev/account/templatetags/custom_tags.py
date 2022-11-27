# import inspect

import config.cute_logging as clog
from django import template
register = template.Library()


# TODO: make this tag useful
# @register.simple_tag
# def get_info(variable, output_mode='00'):
#     '''Custom tag for frontends
#     output_mode:
#         [0] - only attributes
#         [1] - only methods

#         [0] - print result in console
#         [1] - return list result to frontend
#     '''
#     result = ''
#     for i in inspect.getmembers(variable):
#         if not i[0].startswith('_'):
#             if output_mode[0] == '1' and inspect.ismethod(i[1]):
#                 result += str(i[0]) + '\n'
#             elif output_mode[0] == '0' and not inspect.ismethod(i[1]):
#                     result += str(i[0]) + '\n'

#     if output_mode[1] == '0':
#         print(result)
#         return ''
#     else:
#         return result


@register.simple_tag(takes_context=True)
def get_context(context):
    clog.message(f'\tYour context: {list(context)[0]}', clog.GOOD)
    return ''
