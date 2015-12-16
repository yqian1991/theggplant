theme_create_schema = {
    'type': 'object',
    'properties': {
        'name': {
            'type': ['string'],
            "minLength": 3,
            'required': True
        },
        'image': {
            'type': ['string'],
            'required': False
        },
        'description': {
            'type': ['string'],
            "minLength": 10,
            'required': False
        },
        'css': {
            'type': ['string'],
            'required': False
        },
        'extra':{
            'type': 'object',
            'required': False
        }
    },
    "additionalProperties": False
}

theme_update_schema = {
    'type': 'object',
    'properties': {
        'name': {
            'type': ['string'],
            "minLength": 3,
            'required': False
        },
        'image': {
            'type': ['string'],
            'required': False
        },
        'description': {
            'type': ['string'],
            "minLength": 10,
            'required': False
        },
        'css': {
            'type': ['string'],
            'required': False
        },
        'extra':{
            'type': 'object',
            'required': False
        }
    },
    "additionalProperties": False
}

theme_search_schema = {
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
