user_create_schema = {
    'type': 'object',
    'properties': {
        'email': {
            'type': ['string'],
            'pattern': "[^@]+@[^@]+\.[^@]+",
            'required': True
        },
        'password': {
            'type': ['string'],
            'required': True,
            "minLength": 6
        },
        'group': {
            'type': ['string'],
            'oneOf': ['admin', 'eater', 'chef'],
            'required': True
        }
    },
    "additionalProperties": False
}

user_update_schema = {
    'type': 'object',
    'properties': {
        'email': {
            'type': ['string'],
            'pattern': "[^@]+@[^@]+\.[^@]+",
            'required': False
        },
        'password': {
            'type': ['string'],
            'required': False,
            "minLength": 6
        },
        'extra':{
            'type': 'object',
            'properties': {
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