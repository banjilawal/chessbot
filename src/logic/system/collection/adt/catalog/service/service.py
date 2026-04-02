# src/logic/system/collection/hash/service/validator.py

"""
Module: logic.system.collection.hash.service.service
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from enum import Enum

from logic.system import QueryService, Microservice, Validator


class HashMicroservice(Microservice[Enum]):
    _hash_key_service: QueryService[Enum]
  
    def __init__(
            self,
            id: int,
            name: str,
            validator: Validator[Enum],
            super_key_service: QueryService[Enum],
    ):
        super().__init__(id=id, name=name, certifier=validator)
        self._hash_key_service = super_key_service
        
    @property
    def hash_key_service(self) -> QueryService[Enum]:
        return self._hash_key_service
    
    @property
    def hash_validator(self) -> Validator[Enum]:
        return self.certifier
    