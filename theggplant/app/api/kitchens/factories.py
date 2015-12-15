from pyramid.security import Allow
from pyramid.security import ALL_PERMISSIONS
from pyramid.security import Everyone

from .models import Kitchen


class KitchenFactory(object):
    __acl__ = [
        (Allow, 'g:admin', ALL_PERMISSIONS),
        (Allow, 'g:chef', 'create'),
        (Allow, Everyone, 'search'),
    ]

    def __init__(self, request):
        self.request = request

    def __getitem__(self, key):
        kitchen = Kitchen.get(key)
        if kitchen:
            kitchen.__parent__ = self
            kitchen.__name__ = key
        return kitchen