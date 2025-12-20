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
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing State Machine microservice API.
    2.  Encapsulates integrity assurance logic in one extendable module that's easy to maintain.
    3.  Is authoritative, single-source-of-truth for an entity's state by providing single entry and exit points to
        the entity's lifecycle.
    4.  Bundles  operations that produce different Result subclasses.

    # PARENT:
    None

    # PROVIDES:
        *   entity_builder:  --> Builder[T]
        *   entity_validator: --> Validator[T]

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   designation (str)
        *   builder (Builder[T])
        *   number_bounds_validator (Validator[T])
        
    # INHERITED ATTRIBUTES:
    None
    """
    _id: int
    _name: str
    _builder: Builder[T]
    _validator: Validator[T]
    
    def __init__(
            self,
            id: int,
            name: str,
            builder: Builder[T],
            validator: Validator[T],
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   designation (str)
            *   builder (Builder[T])
            *   number_bounds_validator (Validator[T])

        # Returns:
        None

        # Raises:
        None
        """
        self._id = id
        self._name = name
        self._builder = builder
        self._validator = validator
        
    @property
    def id(self) -> int:
        """get entity id"""
        return self._id
    
    @property
    def name(self) -> str:
        """get entity designation"""
        return self._name
    
    @property
    def entity_builder(self) -> Builder[T]:
        """get entity builder"""
        return self._builder
    
    @property
    def entity_validator(self) -> Validator[T]:
        """get entity number_bounds_validator"""
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
        return f"id:{self._id}, designation:{self._name}"
    
    