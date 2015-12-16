from pyramid.security import Allow
from pyramid.security import ALL_PERMISSIONS
from pyramid.security import Everyone

from .models import Menuitem


class MenuitemFactory(object):
    __acl__ = [
        (Allow, 'g:admin', ALL_PERMISSIONS),
        (Allow, 'g:admin', 'admin_search'),
        (Allow, 'g:chef', 'create'),
        (Allow, Everyone, 'search'),
    ]

    def __init__(self, request):
        self.request = request

    def __getitem__(self, key):
        menuitem = Menuitem.get(key)
        if menuitem:
            menuitem.__parent__ = self
            menuitem.__name__ = key
        return menuitem