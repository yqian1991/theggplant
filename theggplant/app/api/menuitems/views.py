import transaction
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPBadRequest

from theggplant.app.utils import validate_json_input

from .models import Menuitem
from .jsonschemas import (menuitem_create_schema,
    menuitem_update_schema,
    menuitem_search_schema,
    kitchen_menuitem_search_schema
)
from theggplant.app.api.kitchens.models import Kitchen

@view_config(
    route_name='kitchen_menuitem_list',
    permission='view_items',
    renderer='json',
)
@view_config(
    route_name='menuitem_list',
    permission='list',
    renderer='json',
)
def menuitem_list(request):
    kitchen_id = request.matchdict.get('kitchen_id')
    if kitchen_id:
        return Menuitem.filter(kitchen_id=kitchen_id)
    return Menuitem.list()

@view_config(
    route_name='get_menuitem',
    permission='view',
    renderer='json',
)
def get_menuitem(request):
    id = request.matchdict['id']
    menuitem = Menuitem.get(id)
    if not menuitem:
        raise HTTPNotFound()
    return menuitem

@view_config(
    route_name='delete_menuitem',
    permission='delete',
    renderer='json',
)
def delete_menuitem(request):
    id = request.matchdict['id']
    menuitem = Menuitem.delete(id)
    if not menuitem:
        raise HTTPNotFound()
    return menuitem

@view_config(
    route_name='update_menuitem',
    permission='update',
    renderer='json',
)
@validate_json_input(menuitem_update_schema)
def update_menuitem(request):
    id = request.matchdict['id']
    if request.user.group != 'admin' and 'kitchen_id' in request.json and (
        request.json['kitchen_id'] not in [k.id for k in request.user.kitchens.all()]
    ):
        raise HTTPBadRequest()
    Menuitem.update(id, request.json)
    return {}

@view_config(
    route_name='create_menuitem',
    permission='create',
    renderer='json',
)
@validate_json_input(menuitem_create_schema)
def create_menuitem(request):
    _ = request.translate
    if request.user.group != 'admin' and 'kitchen_id' in request.json and (
        request.json['kitchen_id'] not in [k.id for k in request.user.kitchens.all()]
    ):
        raise HTTPBadRequest()
    data = request.json
    menuitem = Menuitem.create(data)
    return menuitem

@view_config(
    route_name='search_menuitems',
    permission='admin_search',
    renderer='json',
)
@validate_json_input(menuitem_search_schema)
def search_menuitems(request):
    _ = request.translate
    query = request.json
    params = []
    if 'kitchen_id' in query:
        name = query.pop('kitchen_id')
        params.append({
            'key': 'kitchen_id',
            'op': '=',
            'value': kitchen_id
        })
    if 'name' in query:
        name = query.pop('name')
        params.append({
            'key': 'name',
            'op': '*',
            'value': name
        })

    total = Menuitem.count(params)
    menuitems = Menuitem.search(params,**query)
    if request.user and request.user.group in ['admin', 'chef']:
        return {
            'total': total,
            'data': menuitems
        }

    data = []
    for menuitem in menuitems:
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

@view_config(
    route_name='search_kitchen_menuitems',
    permission='search',
    renderer='json',
)
@validate_json_input(kitchen_menuitem_search_schema)
def search_kitchen_menuitems(request):
    _ = request.translate
    kitchen_id = request.matchdict['kitchen_id']
    query = request.json
    params = []
    params.append({
        'key': 'kitchen_id',
        'op': '=',
        'value': kitchen_id
    })
    if 'name' in query:
        name = query.pop('name')
        params.append({
            'key': 'name',
            'op': '*',
            'value': name
        })

    total = Menuitem.count(params)
    menuitems = Menuitem.search(params,**query)
    if request.user and request.user.group in ['admin', 'chef']:
        return {
            'total': total,
            'data': menuitems
        }

    data = []
    for menuitem in menuitems:
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



