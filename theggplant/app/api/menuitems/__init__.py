from .factories import MenuitemFactory
from theggplant.app.api.kitchens.factories import KitchenFactory


def includeme(config):
	settings = config.get_settings()
	config.add_route('menuitem_list', '/api/v1/menuitems', request_method=['GET'], factory=MenuitemFactory)
	config.add_route('kitchen_menuitem_list', '/api/v1/kitchens/{kitchen_id}/menuitems', request_method=['GET'], factory=KitchenFactory,
		traverse='/{kitchen_id}')
	config.add_route('create_menuitem', '/api/v1/menuitems', request_method=['POST'], factory=MenuitemFactory)
	config.add_route('get_menuitem', '/api/v1/menuitems/{id}', request_method=['GET'], factory=MenuitemFactory,
                     traverse='/{id}')
	config.add_route('update_menuitem', '/api/v1/menuitems/{id}', request_method=['PUT', 'PATCH'], factory=MenuitemFactory,
                     traverse='/{id}')
	config.add_route('delete_menuitem', '/api/v1/menuitems/{id}', request_method=['DELETE'])
	config.add_route('search_menuitems', '/api/v1/menuitems/search', request_method=['POST'], factory=MenuitemFactory)
	config.add_route('search_kitchen_menuitems', '/api/v1/menuitems/search/{kitchen_id}', request_method=['POST'])