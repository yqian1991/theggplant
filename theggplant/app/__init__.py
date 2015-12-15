def includeme(config):
	settings = config.get_settings()
	config.add_route('account', '/account', request_method=['GET'])
	config.include("theggplant.app.auth")
	config.include("theggplant.app.account")
	config.include("theggplant.app.api")
	config.include("theggplant.app.db")
	config.include("theggplant.app.i18n")
	config.include("theggplant.app.upload")