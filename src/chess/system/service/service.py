# src/chess/system/service/service.py

"""
Module: chess.system.service.service
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from abc import ABC
from typing import Generic, TypeVar

from chess.system import Builder, Validator

T = TypeVar("T")


class EntityService(ABC, Generic[T]):
    """
    # ROLE: Service, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing API.
    2.  Protects objects from direct, unprotected access.
    3.  Encapsulates highly cohesive modules, and operations for easier extension, use and maintenance.
    4.  Provide a single entry point managing an Entity's integrity lifecycle.
    
    # PARENT
    None

    # PROVIDES:
        *   EntityBuilder
        *   EntityValidator

    # ATTRIBUTES:
    None
        *   id (int):
        *   name (str):
        *   _builder (Builder[T]):
        *   _validator (Validator[T]):
    """
    _builder: Builder[T]
    _validator: Validator[T]
    
    def __init__(
            self,
            id: int,
            name: str,
            builder: Builder[T],
            validator: Validator[T],
    ):
        self._id = id
        self._name = name
        self._builder = builder
        self._validator = validator
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def entity_builder(self) -> Builder[T]:
        return self._builder
    
    @property
    def entity_validator(self) -> Validator[T]:
        return self._validator
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, EntityService):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return f"id:{self._id}, name:{self._name}"
    
    