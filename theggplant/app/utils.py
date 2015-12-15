import simplejson as json
import validictory
from functools import wraps
from pyramid.httpexceptions import HTTPBadRequest

def validate_json_input(schema):
    def decorator(func):
        @wraps(func)
        def wrapper(request):
            error = None
            try:
                if request.content_type != 'application/json':
                    msg = 'Request Content-Type must be application/json'
                    raise ValueError(msg)
                data = json.loads(unicode(request.body))
                validictory.validate(data, schema)
            except ValueError as err:
                error = {'error': str(err)}
            except json.JSONDecodeError as err:
                error = {'error': "Corrupted/malformed JSON: %s" % err}
            except validictory.ValidationError as err:
                error = {'error': "Invalid JSON: %s" % err}

            if error is not None:
                return HTTPBadRequest(body=json.dumps(error),
                                      content_type='application/json')

            request.json = data
            return func(request)
        return wrapper
    return decorator
