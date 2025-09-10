# -*- coding: utf-8 -*-

from attrs import define, field, frozen, validators, Factory
from bitstring import Bits


@frozen(kw_only=True)
class SignalDefinition:
    """Represents an immutable definition for a Signal, without any actual value associated

    fields:
    name            -- a human readable name assigned to the Signal
    size            -- the size (in bits) used to represent the Signal value
    offset          -- the signed offset used to convert the raw value into a physical value (default 0)
    factor          -- the factor of multipication to convert the raw value into physical value (default 1)
    min_value       -- the minimum physical value encoded in the Signal
    max_value       -- the maximum physical value encoded in the Signal
    """

    # all defaults and converter values are defined below
    name: str               = field()
    size: int               = field(default=8,
                                    # validator=[validators.instance_of(int),_size_validator],
                                    converter=lambda x : x if x is None else int(x))
    offset: float           = field(default=0,
                                    converter=lambda x : x if x is None else float(x))
    factor: float           = field(default=1,
                                    converter=lambda x : x if x is None else float(x))
    min_value: float        = field(converter=lambda x : x if x is None else float(x))
    _min_value_bits: Bits   = field(init=False)
    _max_value_bits: Bits   = field(init=False)
    max_value: float        = field(converter=lambda x : x if x is None else float(x))

    @min_value.default
    def _min_value_factory(self) -> float:
        return self.offset
        
    @_min_value_bits.default
    def _min_value_bits_factory(self) -> Bits:
        return Bits(length=self.size)
        
    @_max_value_bits.default
    def _max_value_bits_factory(self) -> Bits:
        return Bits(hex=(~self._min_value_bits).hex, length=self.size)
    
    @max_value.default
    def _max_value_factory(self) -> float:
        return self._max_value_bits.uint * self.factor + self.offset        # using a int type, the sign is implicitly given. We don't want that
    
            
    
    @size.validator
    def _size_validator(self, attribute, value):
        if value < 1:
            raise ValueError(f"Size must be at least 1 bit. Problem in SignalDefinition {self.name} where size is {self.size}")

    @max_value.validator
    def _max_value_validator(self, attribute, value):
        if value < self.min_value:
            raise ValueError(f"The attributed min_size is larger than the max_size. Problem in SignalDefinition {self.name} with min {self.min_value} and max {self.max_value}")