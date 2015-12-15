import transaction

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import forget
from pyramid.security import remember
from pyramid.security import authenticated_userid

from sqlalchemy.exc import DBAPIError, IntegrityError

from theggplant.app.api.users.models import User

from .forms import SignupForm, LoginForm


@view_config(
    route_name='sign_up',
    renderer='app/auth/templates/signup.jinja2'
)
def sign_up(request):
    _ = request.translate
    form = SignupForm(request.params, _)

    if request.method == 'POST' and form.validate():
        user = User.create(request.POST, unique=['email'])
        if user is None:
            return {
                'form': form,
                'error': _('The email is already used by another user.')
            }
        headers = forget(request)
        return HTTPFound(location=request.route_url('login'), headers=headers)

    return {'form': form}

@view_config(
    route_name='login',
    renderer='app/auth/templates/login.jinja2',
)
def login(request):
    _ = request.translate
    next = request.params.get('next') or request.route_url('account')
    if request.user:
        return HTTPFound(location=next)
    form = LoginForm(request.params, _)

    if request.method == 'POST' and form.validate():
        users = User.filter(
            deleted=False,
            email=form.email.data
        )
        if users and users[0].check_password(form.password.data):
            headers = remember(request, users[0].id)
            return HTTPFound(location=next, headers=headers)
        return {
            'form': form,
            'error': _('Please enter a correct email and password.')
        }
    return {'form': form}

@view_config(
    route_name='logout',
)
def logout(request):
    headers = forget(request)
    return HTTPFound(location=request.route_url('login'), headers=headers)