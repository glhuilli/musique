JSON_SCHEMA = {
    '$defs': {
        'song': {
            'properties': {
                'artist': {
                    'type': 'string'
                },
                'title': {
                    'type': 'string'
                }
            },
            'required': ['title', 'artist'],
            'type': 'object'
        }
    },
    '$schema': 'https://json-schema.org/draft/2020-12/schema',
    'properties': {
        'songs': {
            'items': {
                '$ref': '#/$defs/song'
            },
            'type': 'array'
        }
    },
    'type': 'object'
}
