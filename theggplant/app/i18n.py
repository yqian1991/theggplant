from pyramid.events import NewRequest
from pyramid.events import subscriber
from webob.acceptparse import Accept
from pyramid.i18n import get_localizer, TranslationStringFactory


def add_renderer_globals(event):
	request = event.get('request')
	if request is None:
		request = get_current_request()
	event['_'] = request.translate
	event['localizer'] = request.localizer

tsf = TranslationStringFactory('theggplant')

def add_localizer(event):
	request = event.request
	localizer = get_localizer(request)

	def auto_translate(string):
		return localizer.translate(tsf(string))
	request.localizer = localizer
	request.translate = auto_translate

def includeme(config):
	settings = config.get_settings()
	config.add_translation_dirs('theggplant:locale')
	config.add_subscriber('theggplant.app.i18n.add_renderer_globals',
						  'pyramid.events.BeforeRender')
	config.add_subscriber('theggplant.app.i18n.add_localizer',
						  'pyramid.events.NewRequest')
