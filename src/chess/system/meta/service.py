# src/chess/system/metadata/service.py

"""
Module: chess.system.metadata.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum

from chess.system import ContextService, ForwardLookup, Service, Validator


class EnumService(Service[Enum]):
    _enum_super_key_service: ContextService[Enum]
    _enum_forward_lookup: ForwardLookup[Enum]
    
    def __init__(
            self,
            id: int,
            name: str,
            validator: Validator[Enum],
            super_key_service: ContextService[Enum], forward_lookup: ForwardLookup[Enum],
    ):
        super().__init__(id=id, name=name, certifier=validator)
        self._enum_super_key_service = super_key_service
        self._enum_forward_lookup = forward_lookup
        
    @property
    def enum_super_key_service(self) -> ContextService[Enum]:
        return self._enum_super_key_service
    
    @property
    def enum_forward_lookup(self) -> ForwardLookup[Enum]:
        return self._enum_forward_lookup
    