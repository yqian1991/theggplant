from pyramid_storage.exceptions import FileNotAllowed
from pyramid.view import view_config
from theggplant.app.utils import validate_json_input


@view_config(route_name='image_upload',
             permission='upload',
             request_method='POST')
def image_upload(request):
    _ = request.translate
    type = request.POST.get('type')
    if not type:
    	return {"error": _('type is missing in the request')}

    image = request.POST['image']
    try:
        path = request.storage.save(
        		image,
            extensions=('jpg', 'png', 'gif'),
            randomize=True,
            folder=type
        )
        return {"file": path}
    except FileNotAllowed:
        return {"error": _('Sorry, this file is not allowed')}
