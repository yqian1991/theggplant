from pyramid.security import Allow
from pyramid.security import ALL_PERMISSIONS
from pyramid.security import Everyone


class UploadFactory(object):
    __acl__ = [
        (Allow, 'g:admin', ALL_PERMISSIONS),
        (Allow, 'g:chef', 'upload')
    ]

    def __init__(self, request):
        self.request = request