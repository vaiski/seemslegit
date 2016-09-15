# -*- coding: utf-8 -*-

from functools import wraps
from .errors import ValidationError


def validator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        fail = kwargs.get('fail', False)
        if 'fail' in kwargs:
            del kwargs['fail']
        valid = func(*args, **kwargs)
        if not valid:
            error = ValidationError(func, args)
            if fail:
                raise error
            return error
        return True
    return wrapper
