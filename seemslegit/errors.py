# -*- coding: utf-8 -*-


class ValidationError(Exception):

    def __init__(self, validator, error):
        self.validator = validator
        self.error = error

    def __bool__(self):
        return False
