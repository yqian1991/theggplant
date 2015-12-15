from .factories import UploadFactory


def includeme(config):
	settings = config.get_settings()
	config.include("pyramid_storage")
	config.add_route('image_upload', '/upload/image', request_method=['POST'], factory=UploadFactory)