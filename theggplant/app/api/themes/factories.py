from pyramid.security import Allow
from pyramid.security import ALL_PERMISSIONS
from pyramid.security import Everyone

from .models import Theme


class ThemeFactory(object):
    __acl__ = [
        (Allow, 'g:admin', ALL_PERMISSIONS),
        (Allow, 'g:chef', ['search', 'view'])
    ]

    def __init__(self, request):
        self.request = request
