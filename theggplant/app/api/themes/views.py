import transaction
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPBadRequest

from theggplant.app.utils import validate_json_input

from .models import Theme
from .jsonschemas import theme_create_schema, theme_update_schema, theme_search_schema

@view_config(
    route_name='theme_list',
    permission='list',
    renderer='json',
)
def theme_list(request):
    return Theme.list()

@view_config(
    route_name='get_theme',
    permission='view',
    renderer='json',
)
def get_theme(request):
    id = request.matchdict['id']
    theme = Theme.get(id)
    if not theme:
        raise HTTPNotFound()
    return theme

@view_config(
    route_name='delete_theme',
    permission='delete',
    renderer='json',
)
def delete_theme(request):
    id = request.matchdict['id']
    theme = Theme.delete(id)
    if not theme:
        raise HTTPNotFound()
    return theme

@view_config(
    route_name='update_theme',
    permission='update',
    renderer='json',
)
@validate_json_input(theme_update_schema)
def update_theme(request):
    id = request.matchdict['id']
    Theme.update(id, request.json)
    return {}

@view_config(
    route_name='create_theme',
    permission='create',
    renderer='json',
)
@validate_json_input(theme_create_schema)
def create_theme(request):
    data = request.json
    theme = Theme.create(data)
    return theme

@view_config(
    route_name='search_themes',
    permission='search',
    renderer='json',
)
@validate_json_input(theme_search_schema)
def search_themes(request):
    _ = request.translate
    query = request.json
    params = []
    if 'name' in query:
        name = query.pop('name')
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
    total = Theme.count(params)
    themes = Theme.search(params, **query)
    return {
        'total': total,
        'data': themes
    }


