def includeme(config):
	settings = config.get_settings()
	config.include("theggplant.app.api.users")
	config.include("theggplant.app.api.kitchens")
	config.include("theggplant.app.api.menuitems")
	config.include("theggplant.app.api.themes")

