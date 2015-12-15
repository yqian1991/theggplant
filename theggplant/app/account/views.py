from pyramid.view import view_config
from pyramid.security import authenticated_userid
from pyramid.httpexceptions import HTTPFound


@view_config(
    route_name='account',
    renderer='app/account/templates/index.jinja2',
)
def account(request):
    if not authenticated_userid(request):
        return HTTPFound(location=request.route_url('login'))
    return {}