# -*- coding: utf-8 -*-

import pytest

from automotive_types.SignalDefinition import SignalDefinition

def test_SignalDefinition_init_vanilla():
    """
    Verifies the standard initialization with expected values for the class
    
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

@pytest.mark.parametrize("name,v_min,v_max,e_min,e_max",
                        [("trivial_int",0,255,0.0,255.0),
                         ("trivial_float",0.0,255.0,0.0,255.0),
                         ("trivial_str","0","255",0.0,255.0),
                         ("trivial_str2","0.0","255.0",0.0,255.0),
                         # ("trivial_str3","0x00","0xFF",0.0,255.0),
                         # ("trivial_None",None,None,0.0,255.0),
                         ("nontrivial_int",1,254,1.0,254.0),
                         ("nontrivial_float",1.0,254.0,1.0,254.0),
                         ("nontrivial_string","1","254",1.0,254.0),
                         ("nontrivial_hex",0x01,0xFE,1.0,254.0),
                         ("trivial_hex",0x00,0xFF,0.0,255.0)
                        ])
def test_SignalDefinition_init_with_min_max(name,v_min,v_max,e_min,e_max):
    """
    Verifies that all parameters can be initialized as valid parameters
    
    GIVEN the parametrized test data covering boundary analysis test cases and defaulting the remainder of inputs
    WHEN instantiating SignalDefinition passing the parametrized min and max value
    THEN all expected inputs should work fine
    """
    xut = SignalDefinition(name=name, min_value=v_min, max_value=v_max)
    assert xut.name == name
    assert xut.size == 8
    assert xut.factor == 1.0
    assert xut.offset == 0.0
    assert xut.min_value == e_min
    assert xut.max_value == e_max