import sqlalchemy as sa
from sqlalchemy.orm import relationship, backref
import sqlalchemy_utils.types as sa_types

from slugify import slugify

from theggplant.app.db import Base, TimestampMixin, PseudoDelete, Crud, JsonType


class Theme(TimestampMixin, PseudoDelete, Crud, Base):
    __tablename__ = 'theme'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False)
    slug = sa.Column(sa.String(255), nullable=False)
    description = sa.Column(sa.Text(), nullable=True)
    active = sa.Column(sa.Boolean(), nullable=False, default=False)
    image = sa.Column(sa.String(1000), nullable=True)
    css = sa.Column(sa.Text(), nullable=True)
    extra = sa.Column(JsonType, nullable=False, default={})

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs:
            kwargs['slug'] = slugify(kwargs.get('name', ''))
        super(Theme, self).__init__(*args, **kwargs)

    def __repr__(self):
        return self.name

    def __json__(self, request):
        return {
            "id": self.id,
            "name": self.name,
            "slug": self.slug,
            "extra": self.extra,
            "description": self.description,
            "css": self.css,
            "active": self.active,
            "image": self.image,
            "deleted": self.deleted,
            "updated_at": self.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            "created_at": self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }