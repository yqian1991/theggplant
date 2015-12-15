import json
import datetime
import transaction
import sqlalchemy as sa
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import engine_from_config

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension(),expire_on_commit=False))
Base = declarative_base()


def includeme(config):
	settings = config.get_settings()
	engine = engine_from_config(settings, 'sqlalchemy.')
	DBSession.configure(bind=engine)
	Base.metadata.bind = engine

class TimestampMixin(object):
	updated_at = sa.Column(sa.DateTime, default=lambda: datetime.datetime.utcnow(),onupdate=lambda: datetime.datetime.utcnow())
	created_at = sa.Column(sa.DateTime, default=lambda: datetime.datetime.utcnow())

class PseudoDelete(object):
	deleted = sa.Column(sa.Boolean, default=False)

class Crud(object):
	@classmethod
	def get(cls, id):
		return DBSession.query(cls).filter(cls.id == id).first()

	@classmethod
	def create(cls, data):
		try:
			with transaction.manager:
				new = cls(**data)
				DBSession.add(new)
		except IntegrityError:
			return None
		return new

	@classmethod
	def list(cls):
		return DBSession.query(cls).all()

	@classmethod
	def update(cls, id, data):
		with transaction.manager:
			DBSession.query(cls).filter(cls.id == id).update(data)

	@classmethod
	def delete(cls, id):
		existing = DBSession.query(cls).filter(cls.id == id).first()
		with transaction.manager:
			if hasattr(existing, 'deleted'):
				existing.deleted = True
			else:
				DBSession.delete(existing)
		return existing

	@classmethod
	def search(cls, params, start=0, rows=10, orderby='id', orderdir='asc'):
		query = DBSession.query(cls)
		for item in params:
			key = item['key']
			op = item['op']
			value = item['value']
			if op == '*':
				query = query.filter(getattr(cls, key).ilike("%%%s%%" % value))
			elif op == '=':
				query = query.filter(getattr(cls, key) == value)
		if hasattr(cls, 'deleted'):
			query = query.filter(cls.deleted==False)

		query = query.order_by(
			getattr(cls, orderby).asc() if orderdir=='asc' else getattr(cls, orderby).desc()
		)
		return query.offset(start).limit(rows).all()

	@classmethod
	def count(cls, params):
		query = DBSession.query(cls)
		for item in params:
			key = item['key']
			op = item['op']
			value = item['value']
			if op == '*':
				query = query.filter(getattr(cls, key).ilike("%%%s%%" % value))
			elif op == '=':
				query = query.filter(getattr(cls, key) == value)
		if hasattr(cls, 'deleted'):
			query = query.filter(cls.deleted==False)

		return query.count()

	@classmethod
	def filter(cls, **params):
		query = DBSession.query(cls)
		for key, value in params.iteritems():
			if value:
				query = query.filter(getattr(cls, key)==value)
		return query.all()

class JsonType(sa.types.TypeDecorator):
	impl = sa.types.UnicodeText

	def process_bind_param(self, value, engine):
		return unicode(json.dumps(value))

	def process_result_value(self, value, engine):
		if value:
			return json.loads(value)
		else:
			# default can also be a list
			return {}
