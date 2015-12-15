import transaction
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound

from theggplant.app.utils import validate_json_input

from .models import User
from .jsonschemas import user_create_schema, user_update_schema


@view_config(
    route_name='user_list',
    permission='list',
    renderer='json',
)
def user_list(request):
    return User.list()

@view_config(
    route_name='get_user',
    permission='view',
    renderer='json',
)
def get_user(request):
    id = request.matchdict['id']
    user = User.get(id)
    if not user:
        raise HTTPNotFound()
    return user

@view_config(
    route_name='delete_user',
    permission='delete',
    renderer='json',
)
def delete_user(request):
    id = request.matchdict['id']
    user = User.delete(id)
    if not user:
        raise HTTPNotFound()
    return user

@view_config(
    route_name='update_user',
    permission='update',
    renderer='json',
)
@validate_json_input(user_update_schema)
def update_user(request):
    id = request.matchdict['id']
    User.update(id, request.json)
    return {}

@view_config(
    route_name='create_user',
    permission='create',
    renderer='json',
)
@validate_json_input(user_create_schema)
def create_user(request):
    _ = request.translate
    user = User.create(request.json)
    if not user:
        return {
            "error": _("The email is already used by another user.")
        }
    return user
