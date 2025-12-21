# src/chess/system/lookup/service/service.py

"""
Module: chess.system.lookup.service.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""


from enum import Enum

from chess.system import Builder, Context, ContextService, ForwardLookup, Validator
from chess.system.lookup.reverse import ReverseLookup


class LookupService(ContextService[Context[Enum]]):
    _forward_lookup: ForwardLookup
    _reverse_lookup: ReverseLookup
    
    def service(
            self,
            id: int,
            name: str,
            builder: Builder[Context[Enum]],
            validator: Validator[Context[Enum]],
            forward_lookup: ForwardLookup,
            reverse_lookup: ReverseLookup
    ):
        super().service(id=id, name=name, builder=builder, validator=validator)
        self._forward_lookup = forward_lookup
        self._reverse_lookup = reverse_lookup
        
    @property
    def forward_lookup(self) -> ForwardLookup:
        return self._forward_lookup
    
    @property
    def __reversed__(self) -> ReverseLookup:
        return self._reverse_lookup