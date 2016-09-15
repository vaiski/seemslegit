# -*- coding: utf-8 -*-

import pytest
from seemslegit import (
    validator, ValidationError
)


@validator
def positive(value):
    return value > 0


def test_raise_error():
    with pytest.raises(ValidationError,
                       message="Expecting ValidationError when fail=True"):
        positive(-55, fail=True)


def test_return_error():
    assert not positive(-55), "Return value was truthy, should be falsy"


def test_return_truthy():
    assert positive(1), "Return value was falsy, should be truthy"
