def includeme(config):
	settings = config.get_settings()
	config.add_route('account', '/account', request_method=['GET'])
