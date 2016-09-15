# -*- coding: utf-8 -*-


class ValidationError(Exception):

    def __init__(self, validator, value):
        self.validator = validator
        self.value = value

    def __len__(self):
        return 0

    def __nonzero__(self):
        return False

    def __bool__(self):
        return False

    def __str__(self):
        return "Value {} didn't satisfy validator {}".format(
            self.value,
            self.validator.__name__
        )
