# -*- coding: utf-8 -*-

import pytest

from automotive_types.SignalDefinition import SignalDefinition

def test_SignalDefinition_init():
    """Validates the standard initialization with expected values for the class
    GIVEN N/A
    WHEN instantiating SignalDefinition passing only the name keyword
    THEN all other parameters are inferred as:
                    size=8,
                    factor=1.0,
                    offset=0.0,
                    min_value=0.0,
                    max_value=255.0
    """
    xut = SignalDefinition(name="xut")
    assert xut.name == "xut"
    assert xut.size == 8
    assert xut.factor == 1.0
    assert xut.offset == 0.0
    assert xut.min_value == 0.0
    assert xut.max_value == 255.0