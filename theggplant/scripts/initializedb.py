import os
import sys
import random
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from theggplant.app.db import (
    DBSession,
    Base
    )
from theggplant.app.api.users.models import User
from theggplant.app.api.kitchens.models import Kitchen
from theggplant.app.api.menuitems.models import Menuitem
from theggplant.app.api.themes.models import Theme



def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        model = User(email='admin@gmail.com', password='123', group='admin')
        DBSession.add(model)
        model = User(email='chef1@gmail.com', password='123', group='chef')
        DBSession.add(model)
        model = User(email='chef2@gmail.com', password='123', group='chef')
        DBSession.add(model)
    with transaction.manager:
        model = Theme(name='Beautiful', css='.name{color: #f00;}', description='Very Beautiful')
        DBSession.add(model)
        model = Theme(name='Cool', css='.name{color: #0f0;}', description='Very Cool')
        DBSession.add(model)
        model = Theme(name='Dark', css='.name{color: #000;}', description='Very dark')
        DBSession.add(model)
    with transaction.manager:
        for i in range(50):
            model = Kitchen(name='Noodle House %s' % i, style='cantonese', thumbnail='thumbnail%s.png' % i, owner_id=random.choice([2,3]), extra={'phone': '1234567'})
            DBSession.add(model)
    with transaction.manager:
        for i in range(50):
            for j in range(20):
                model = Menuitem(name='Noodle %s' % j, thumbnail='thumbnail%s.png' % j, kitchen_id=i)
                DBSession.add(model)
