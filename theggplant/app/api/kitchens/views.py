import transaction
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPBadRequest

from theggplant.app.utils import validate_json_input

from .models import Kitchen
from .jsonschemas import kitchen_create_schema, kitchen_update_schema, kitchen_search_schema
from theggplant.app.api.kitchens.models import User


@view_config(
    route_name='kitchen_list',
    permission='list',
    renderer='json',
)
def kitchen_list(request):
    return Kitchen.list()

@view_config(
    route_name='get_kitchen',
    permission='view',
    renderer='json',
)
def get_kitchen(request):
    id = request.matchdict['id']
    kitchen = Kitchen.get(id)
    if not kitchen:
        raise HTTPNotFound()
    return kitchen

@view_config(
    route_name='delete_kitchen',
    permission='delete',
    renderer='json',
)
def delete_kitchen(request):
    id = request.matchdict['id']
    kitchen = Kitchen.delete(id)
    if not kitchen:
        raise HTTPNotFound()
    return kitchen

@view_config(
    route_name='update_kitchen',
    permission='update',
    renderer='json',
)
@validate_json_input(kitchen_update_schema)
def update_kitchen(request):
    id = request.matchdict['id']
    if request.user.group != 'admin' and 'owner_id' in request.json \
        and request.user.id != request.json['owner_id']:
        raise HTTPBadRequest()
    if request.user.group != 'admin' and 'active' in request.json:
        raise HTTPBadRequest()
    Kitchen.update(id, request.json)
    return {}

@view_config(
    route_name='create_kitchen',
    permission='create',
    renderer='json',
)
@validate_json_input(kitchen_create_schema)
def create_kitchen(request):
    _ = request.translate
    if request.user.group != 'admin' and 'owner_id' in request.json \
        and request.user.id != request.json['owner_id']:
        raise HTTPBadRequest()
    data = request.json
    if 'owner_id' not in data:
        data['owner_id'] = request.user.id
    user = User.get(data['owner_id'])
    if not user:
       return {
            "error": _("The specified owner is not found.")
        }
    if user.kitchens.all():
        return {
            "error": _("One kitchen is only allowed to create for the same user.")
        }
    kitchen = Kitchen.create(data)
    return kitchen

@view_config(
    route_name='search_kitchens',
    permission='search',
    renderer='json',
)
@validate_json_input(kitchen_search_schema)
def search_kitchens(request):
    post_data = request.json
    params = []
    if 'name' in post_data:
        name = post_data.pop('name')
        params.append({
            'key': 'name',
            'op': '*',
            'value': name
        })
    if request.user.group != 'admin':
        params.append({
            'key': 'active',
            'op': '=',
            'value': True
        })
        params.append({
            'key': 'deleted',
            'op': '=',
            'value': False
        })
    total = Kitchen.count(params)
    kitchens = Kitchen.search(params,**post_data)
    if request.user and request.user.group in ['admin', 'chef']:
        return {
            'total': total,
            'data': kitchens
        }

    data = []
    for kitchen in kitchens:
        data.append({
            'id': kitchen.id,
            'slug': kitchen.slug,
            'name': kitchen.name,
            'thumbnail': kitchen.thumbnail
        })

    return {
        'total': total,
        'data': data
    }



