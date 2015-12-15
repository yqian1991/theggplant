from pyramid.security import Allow
from pyramid.security import Everyone

import sqlalchemy as sa
from sqlalchemy.orm import relationship, backref
import sqlalchemy_utils.types as sa_types

from slugify import slugify

from theggplant.app.db import Base, TimestampMixin, PseudoDelete, Crud, JsonType
from theggplant.app.api.users.models import User

def get_kitchen_styles(request):
    _ = request.translate if request else (lambda a: a)
    return {
        'snack': _('Snack'),
        'sichuan': _('Sichuan'),
        'dongbei': _('Dongbei'),
        'xiang': _('Xiang'),
        'jiazhe': _('Jiangzhe'),
        'xibei': _('Xibei'),
        'lu': _('Lu'),
        'cantonese': _('Cantonese'),
        'other': _('Other')
    }

class Kitchen(TimestampMixin, PseudoDelete, Crud, Base):
    @property
    def __acl__(self):
        return [
            (Allow, self.owner_id, ('view','update', 'view_items'))
        ]
    __tablename__ = 'kitchen'

    id = sa.Column(sa.Integer, primary_key=True)
    owner_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    owner = sa.orm.relationship(User, backref=sa.orm.backref('kitchens', lazy='dynamic'))
    name = sa.Column(sa.String(255), nullable=False)
    slug = sa.Column(sa.String(255), nullable=False)
    description = sa.Column(sa.Text(), nullable=True)
    active = sa.Column(sa.Boolean(), nullable=False, default=False)
    logo = sa.Column(sa.String(1000), nullable=True)
    thumbnail = sa.Column(sa.String(1000), nullable=True)
    style = sa.Column(sa.String(255), nullable=False)
    extra = sa.Column(JsonType, nullable=False, default={})

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        super(Kitchen, self).__init__(*args, **kwargs)

    def __repr__(self):
        return self.name

    def __json__(self, request):
        return {
            "id": self.id,
            "name": self.name,
            "owner_id": self.owner_id,
            "slug": self.slug,
            "logo": self.logo,
            "extra": self.extra,
            "deleted": self.deleted,
            "description": self.description,
            "active": self.active,
            "thumbnail": self.thumbnail,
            "style": self.style,
            "updated_at": self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }