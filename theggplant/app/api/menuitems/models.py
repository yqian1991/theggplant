from pyramid.security import Allow
from pyramid.security import Everyone

import sqlalchemy as sa
from sqlalchemy.orm import relationship, backref
import sqlalchemy_utils.types as sa_types

from slugify import slugify

from theggplant.app.db import Base, TimestampMixin, PseudoDelete, Crud, JsonType
from theggplant.app.api.kitchens.models import Kitchen


class Menuitem(TimestampMixin, PseudoDelete, Crud, Base):
    @property
    def __acl__(self):
        return [
            (Allow, self.kitchen.owner_id, ('view','update'))
        ]
    __tablename__ = 'menuitem'

    id = sa.Column(sa.Integer, primary_key=True)
    kitchen_id = sa.Column(sa.Integer, sa.ForeignKey('kitchen.id'), nullable=False)
    kitchen = sa.orm.relationship(Kitchen, backref=sa.orm.backref('menuitems', lazy='dynamic'))
    name = sa.Column(sa.String(255), nullable=False)
    slug = sa.Column(sa.String(255), nullable=False)
    description = sa.Column(sa.Text(), nullable=True)
    active = sa.Column(sa.Boolean(), nullable=False, default=False)
    image = sa.Column(sa.String(1000), nullable=True)
    thumbnail = sa.Column(sa.String(1000), nullable=True)
    cooktime = sa.Column(sa.Integer, nullable=True)
    regular_price = sa.Column(sa.Float, nullable=True)
    discount_price = sa.Column(sa.Float, nullable=True)
    extra = sa.Column(JsonType, nullable=False, default={})

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        super(Menuitem, self).__init__(*args, **kwargs)

    def __repr__(self):
        return self.name

    def __json__(self, request):
        return {
            "id": self.id,
            "name": self.name,
            "kitchen_id": self.kitchen_id,
            "slug": self.slug,
            "extra": self.extra,
            "description": self.description,
            "active": self.active,
            "image": self.image,
            "thumbnail": self.thumbnail,
            "cooktime": self.cooktime,
            "deleted": self.deleted,
            "updated_at": self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }