from pyramid.security import Allow

import sqlalchemy as sa
from sqlalchemy.orm import relationship, backref
import sqlalchemy_utils.types as sa_types

from theggplant.app.db import Base, TimestampMixin, PseudoDelete, Crud, JsonType


class User(TimestampMixin, PseudoDelete, Crud, Base):
    @property
    def __acl__(self):
        return [
            (Allow, self.id, ('update','view'))
        ]
    __tablename__ = 'user'
    __table_args__ = (sa.schema.UniqueConstraint('email'),)

    id = sa.Column(sa.Integer, primary_key=True)
    nickname = sa.Column(sa.String(255), nullable=True)
    email = sa.Column(sa.String(255), nullable=False)
    password = sa.Column(sa_types.PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],

        deprecated=['md5_crypt']
    ))
    last_login = sa.Column(sa.DateTime, nullable=True)
    first_name = sa.Column(sa.String(255), nullable=True)
    last_name = sa.Column(sa.String(255), nullable=True)
    group = sa.Column(sa.String(10), nullable=False, default='chef')
    extra = sa.Column(JsonType, nullable=False, default={})

    def check_password(self, password):
        return self.password == password

    def __repr__(self):
        return self.nickname or self.email

    def __json__(self, request):
        return {
            "id": self.id,
            "email": self.email,
            "nickname": self.nickname,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "group": self.group,
            "deleted": self.deleted,
            "extra": self.extra,
            "updated_at": self.updated_at,
            "created_at": self.created_at
        }