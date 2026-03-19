# src/logic/system/collection/hash/service/service.py

"""
Module: logic.system.collection.hash.service.service
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from enum import Enum

from logic.system import ContextService, Service, ValidationProcess


class HashService(Service[Enum]):
    _hash_key_service: ContextService[Enum]
  
    def __init__(
            self,
            id: int,
            name: str,
            validator: ValidationProcess[Enum],
            super_key_service: ContextService[Enum],
    ):
        super().__init__(id=id, name=name, certifier=validator)
        self._hash_key_service = super_key_service
        
    @property
    def hash_key_service(self) -> ContextService[Enum]:
        return self._hash_key_service
    
    @property
    def hash_validator(self) -> ValidationProcess[Enum]:
        return self.certifier
    