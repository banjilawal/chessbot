# src/chess/system/service/integrity.py

"""
Module: chess.system.service.integrity
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from typing import TypeVar

from chess.system import Builder, Service, Validator

T = TypeVar("T")


class IntegrityService(Service[T]):
    """
    # ROLE: IntegrityService, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Provide a single interface/entry point for T objects and modules.
    2.  Masks implementation details and business logic making features easier to use.
    3.  Protects T objects from direct, unprotected access.
    4.  Public facing API.

    # PROVIDES:
    Validator for T
    Building of T objects.

    # ATTRIBUTES:
    None
        *   id (int):
        *   name (str):
        *   item_builder (type[Builder[T]]):
        *   item_validator (type[Validator[T]]):
    """
    _item_builder: Builder[T]
    _item_validator: Validator[T]
    
    def __init__(
            self,
            id: int,
            name: str,
            builder: Builder[T],
            validator: Validator[T]
    ) -> None:
        super().__init__(id=id, name=name)
        self._item_builder = builder
        self._item_validator = validator

    @property
    def item_validator(self) -> Validator[T]:
        return self._item_validator
    
    @property
    def item_builder(self) -> Builder[T]:
        return self._item_builder
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, IntegrityService):
            return self._int == other._int
        return False
    
    def __hash__(self):
        return hash(self._int)
    
    def __str__(self):
        return f"id:{self._id}, name:{self._name}"
    
    