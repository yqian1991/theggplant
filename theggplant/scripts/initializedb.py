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
        model = User(email='dak@surveymonkey.com', password='123', group='admin')
        DBSession.add(model)
        model = User(email='dkuang1980@gmail.com', password='123', group='chef')
        DBSession.add(model)
        model = User(email='biscan607@gmail.com', password='123', group='chef')
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
