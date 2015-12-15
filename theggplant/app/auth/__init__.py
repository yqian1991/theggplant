from pyramid.security import authenticated_userid
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from .factories import RootFactory
from theggplant.app.api.users.models import User

def groupfinder(id, request):
    user = User.get(id)
    if user:
        return ["g:%s" % user.group]

def add_user_id(request):
    user_id = authenticated_userid(request)
    if user_id:
        return User.get(user_id)
    return None


def includeme(config):
    settings = config.get_settings()

    authn_policy = AuthTktAuthenticationPolicy(
        settings['auth.secret'],
        callback=groupfinder,
    )
    authz_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.set_root_factory(RootFactory)

    config.add_request_method(add_user_id, 'user', reify=True)

    config.add_route('sign_up', '/signup', request_method=['POST', 'GET'])
    config.add_route('login', '/login', request_method=['POST', 'GET'])
    config.add_route('logout', '/logout', request_method=['GET'])