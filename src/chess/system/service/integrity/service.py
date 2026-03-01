# src/chess/system/service/integrity/service.py

"""
Module: chess.system.service.integrity.service
Author: Banji Lawal
Created: 2025-11-18
"""

from abc import ABC
from typing import Generic, TypeVar

from chess.system import Service, Builder, Validator

T = TypeVar("T")


class IntegrityService(ABC, Service[Generic[T]]):
    """
    # ROLE: Microservice API, Integrity Lifecycle Manager, APLifecycle Management.

    # RESPONSIBILITIES:
    1.  Integrity Lifecycle Management Microservice API.
    2.  Bundles primitives for assuring integrity and consistency in the two phases of
        the integrity lifecycle.
            *   At object creation.
            *   At object invocation.

    # PARENT:
        *   Service

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   builder (Builder[T])
        *   validator (Validator[T])
        
    # INHERITED ATTRIBUTES:
        *   See Service class for inherited attributes.
        
    # CONSTRUCTOR PARAMETERS:
        *   id (int)
        *   name (name)
        *   builder (Builder[T])
        *   validator (Validator[T])
        
    # LOCAL METHODS:
    None
    
    # INHERITED METHODS:
    *   See Service class for inherited methods.
    """
    _builder: Builder[T]
    _validator: Validator[T]
    
    def __init__(
            self,
            id: int,
            name: str,
            builder: Builder[T],
            validator: Validator[T]
    ):
        super().__init__(id=id, name=name,)
        self._builder = builder
        self._validator = validator
    
    @property
    def builder(self) -> Builder[T]:
        return self._builder
    
    @property
    def validator(self) -> Validator[T]:
        return self.certifier
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, IntegrityService):
                return True
        return False

    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return f"id:{self._id}, name:{self._name}"
