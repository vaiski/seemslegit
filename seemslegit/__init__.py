# -*- coding: utf-8 -*-

__version__ = '0.1.0'

from .validator import validator  # noqa
from .errors import ValidationError  # noqa

__all__ = ['validator', 'ValidationError']
