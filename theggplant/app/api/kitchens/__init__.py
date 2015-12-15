from .factories import KitchenFactory


def includeme(config):
	settings = config.get_settings()
	config.add_route('kitchen_list', '/api/v1/kitchens', request_method=['GET'])
	config.add_route('create_kitchen', '/api/v1/kitchens', request_method=['POST'], factory=KitchenFactory)
	config.add_route('get_kitchen', '/api/v1/kitchens/{id}', request_method=['GET'], factory=KitchenFactory,
                     traverse='/{id}')
	config.add_route('update_kitchen', '/api/v1/kitchens/{id}', request_method=['PUT', 'PATCH'], factory=KitchenFactory,
                     traverse='/{id}')
	config.add_route('delete_kitchen', '/api/v1/kitchens/{id}', request_method=['DELETE'])
	config.add_route('search_kitchens', '/api/v1/kitchens/search', request_method=['POST'], factory=KitchenFactory)