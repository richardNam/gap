from collections import namedtuple

__all__ = [
        'Sample'
        ]


class Sample(namedtuple(
    'Sample', 
    [
        'id', 
        'text', 
        'pronoun', 
        'pronoun_offset', 
        'a', 
        'a_offset', 
        'a_coref', 
        'b', 
        'b_offset', 
        'b_coref', 
        'url'
    ])):
    pass

