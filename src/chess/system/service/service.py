# src/chess/system/entity_service/entity_service.py

"""
Module: chess.system.entity_service.entity_service
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
    # ROLE: EntityService, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Provide a single interface/entry point for modules and objects responsible for a stage in the Entity's
        lifecycle.
    2.  Masks implementation details and business logic making features easier to use.
    3.  Protects T objects from direct, unprotected access.
    4.  Public facing API.
    
    # PARENT
    None

    # PROVIDES:
        *   EntityBuilder
        *   EntityValidator

    # ATTRIBUTES:
    None
        *   id (int):
        *   name (str):
        *   item_builder (type[Builder[T]]):
        *   item_validator (type[Validator[T]]):
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
    def item_builder(self) -> Builder[T]:
        return self._builder
    
    @property
    def item_validator(self) -> Validator[T]:
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
    
    