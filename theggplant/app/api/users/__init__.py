from .factories import UserFactory


def includeme(config):
	settings = config.get_settings()
	config.add_route('user_list', '/api/v1/users', request_method=['GET'])
	config.add_route('create_user', '/api/v1/users', request_method=['POST'])
	config.add_route('get_user', '/api/v1/users/{id}', request_method=['GET'], factory=UserFactory,
                     traverse='/{id}')
	config.add_route('update_user', '/api/v1/users/{id}', request_method=['PUT', 'PATCH'], factory=UserFactory,
                     traverse='/{id}')
	config.add_route('delete_user', '/api/v1/users/{id}', request_method=['DELETE'])
