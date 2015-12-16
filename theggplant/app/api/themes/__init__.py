from .factories import ThemeFactory


def includeme(config):
	settings = config.get_settings()
	config.add_route('theme_list', '/api/v1/themes', request_method=['GET'])
	config.add_route('create_theme', '/api/v1/themes', request_method=['POST'])
	config.add_route('get_theme', '/api/v1/themes/{id}', request_method=['GET'], factory=ThemeFactory)
	config.add_route('update_theme', '/api/v1/themes/{id}', request_method=['PUT', 'PATCH'], factory=ThemeFactory)
	config.add_route('delete_theme', '/api/v1/themes/{id}', request_method=['DELETE'])
	config.add_route('search_themes', '/api/v1/themes/search', request_method=['POST'], factory=ThemeFactory)
