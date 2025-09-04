# -*- coding: utf-8 -*-

import attrs
from bitstring import Bits

@attrs.define
class Signal():
    """Represents a mutable Signal type in an automotive network
    
    fields:
    name   -- a human readable name assigned to the Signal
    size   -- the size (in bits) used to represent the Signal value
    value  -- the raw value (as an integer number) stored in the Signal
    offset -- the signed offset used to convert the raw value into a physical value (default 0)
    factor -- the factor of multipication to convert the raw value into physical value (default 1)
    min    -- the minimum physical value encoded in the Signal
    max    -- the maximum physical value encoded in the Signal
    phys   -- the converted physical value (computed value, do not initialize)
    """
    
    name = attrs.field(default="")
    size = attrs.field(default=8)
    value = attrs.field(default=0)
    offset = attrs.field(default=0)
    factor = attrs.field(default=1)
    min = attrs.field(default=attrs.Factory(lambda self: self.value*self.factor-self.offset, takes_self=True)
    _min_value_bits = attrs.field(default=attrs.Factory(lambda self: BitArray(lenght=self.size), takes_self=True)
    _max_value_bits = attrs.field(default=attrs.Factory(lambda self: self._min_value_bits.invert(), takes_self=True)
    max = attrs.field(default=attrs.Factory(lambda self: self.max_value_bits.int*self.factor+self.offset, takes_self=True)
    