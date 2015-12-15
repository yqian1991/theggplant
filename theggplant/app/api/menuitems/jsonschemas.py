menuitem_create_schema = {
    'type': 'object',
    'properties': {
        'name': {
            'type': ['string'],
            "minLength": 3,
            'required': True
        },
        'kitchen_id': {
            'type': ['integer', 'string'],
            'required': True
        },
        'image': {
            'type': ['string'],
            'required': False
        },
        'thumbnail':{
            'type': ['string'],
            'required': False
        },
        'description': {
            'type': ['string'],
            "minLength": 10,
            'required': False
        },
        'cooktime': {
            'type': ['string'],
            "minLength": 10,
            'required': False
        },
        'extra':{
            'type': 'object',
            'required': False
        }
    },
    "additionalProperties": False
}

menuitem_update_schema = {
    'type': 'object',
    'properties': {
        'name': {
            'type': ['string'],
            "minLength": 3,
            'required': False
        },
        'kitchen_id': {
            'type': ['integer', 'string'],
            'required': False
        },
        'image': {
            'type': ['string'],
            'required': False
        },
        'thumbnail':{
            'type': ['string'],
            'required': False
        },
        'description': {
            'type': ['string'],
            "minLength": 10,
            'required': False
        },
        'cooktime': {
            'type': ['string'],
            "minLength": 10,
            'required': False
        },
        'extra':{
            'type': 'object',
            'required': False
        },
        'active': {
            'type': ['boolean'],
            'required': False,
        }
    },
    "additionalProperties": False
}

menuitem_search_schema = {
    'type': 'object',
    'properties': {
        'name': {
            'type': ['string'],
            'required': False
        },
        'kitchen_id':{
            'type': ['integer'],
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

kitchen_menuitem_search_schema = {
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