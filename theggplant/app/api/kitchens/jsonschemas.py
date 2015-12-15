from .models import get_kitchen_styles


kitchen_create_schema = {
    'type': 'object',
    'properties': {
        'name': {
            'type': ['string'],
            "minLength": 3,
            'required': True
        },
        'owner_id': {
            'type': ['integer', 'string'],
            'required': False
        },
        'logo': {
            'type': ['string'],
            'required': False
        },
        'thumbnail': {
            'type': ['string'],
            'required': False
        },
        'description': {
            'type': ['string'],
            "minLength": 10,
            'required': False
        },
        'style':{
            'type': ['string'],
            'oneOf': get_kitchen_styles(None).keys(),
            'required': True
        },
        'extra':{
            'type': 'object',
            'properties': {
                'address': {
                    'type': ['string'],
                    'required': False
                },
                'phone': {
                    'type': ['string'],
                    'required': False
                },
                'wechat': {
                    'type': ['string'],
                    'required': False
                }
            }
        }
    },
    "additionalProperties": False
}

kitchen_update_schema = {
    'type': 'object',
    'properties': {
        'name': {
            'type': ['string'],
            "minLength": 3,
            'required': False
        },
        'owner_id': {
            'type': ['string', 'integer'],
            'required': False
        },
        'logo': {
            'type': ['string'],
            'required': False
        },
        'active': {
            'type': ['boolean'],
            'required': False,
        },
        'thumbnail': {
            'type': ['string'],
            'required': False
        },
        'description': {
            'type': ['string'],
            "minLength": 10,
            'required': False
        },
        'style':{
            'type': ['string'],
            'oneOf': get_kitchen_styles(None).keys(),
            'required': False
        },
        'extra':{
            'type': 'object',
            'required': False,
            'properties': {
                'address': {
                    'type': ['string'],
                    'required': False
                },
                'phone': {
                    'type': ['string'],
                    'required': False
                },
                'wechat': {
                    'type': ['string'],
                    'required': False
                }
            }
        }
    },
    "additionalProperties": False
}

kitchen_search_schema = {
    'type': 'object',
    'properties': {
        'name': {
            'type': ['string'],
            'required': False
        },
        'start':{
            'type': ['integer'],
            'required': False
        },
        'rows':{
            'type': ['integer'],
            'required': False
        },
        'orderby':{
            'type': ['string'],
            'required': False
        },
        'orderdir':{
            'type': ['string'],
            'required': False
        }
    },
    "additionalProperties": False
}