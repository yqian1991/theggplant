from pyramid.security import Allow
from pyramid.security import ALL_PERMISSIONS

from .models import User


class UserFactory(object):
    __acl__ = [
        (Allow, 'g:admin', ALL_PERMISSIONS),
    ]

    def __init__(self, request):
        self.request = request

    def __getitem__(self, key):
        user = User.get(key)
        if user:
            user.__parent__ = self
            user.__name__ = key
        return user