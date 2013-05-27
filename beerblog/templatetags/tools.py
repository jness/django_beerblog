from django import template

register = template.Library()

@register.filter
def getNonPageArgs(request):
    """return get all GET args"""
    args = []
    print request
    if request.GET:
        for key, value in request.GET.items():
            if key != 'page':
                args.append('&%s=%s' % (key, value))
        return ''.join(args)
    return ''
