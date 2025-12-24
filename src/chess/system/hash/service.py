# src/chess/system/hash/service.py

"""
Module: chess.system.hash.service
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum

from chess.system import ContextService, Service, Validator


class HashService(Service[Enum]):
    _hash_super_key_service: ContextService[Enum]

    
    def __init__(
            self,
            id: int,
            name: str,
            validator: Validator[Enum],
            super_key_service: ContextService[Enum],
    ):
        super().__init__(id=id, name=name, certifier=validator)
        self._hash_super_key_service = super_key_service
        
    @property
    def hash_super_key_service(self) -> ContextService[Enum]:
        return self._hash_super_key_service
    
    @property
    def hash_validator(self) -> Validator[Enum]:
        return self.certifier
    