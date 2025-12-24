# src/chess/system/service/entity/service.py

"""
Module: chess.system.service.entity.service
Author: Banji Lawal
Created: 2025-11-18
"""

from abc import ABC
from typing import Generic, TypeVar

from chess.system import Builder, Service, Validator

T = TypeVar("T")


class EntityService(ABC, Service[Generic[T]]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Public facing microservice API.
    2.  Encapsulate integrity assurance logic in one extendable module.
    3.  Is authoritative, single-source-of-truth for an entity's state by providing single entry and exit points to
        the entity's lifecycle.
    4.  Bundles  operations that produce different Result subclasses.

    # PARENT:
    Service

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   builder (Builder[T])
        
    # INHERITED ATTRIBUTES:
        *   See Service class for inherited attributes.
    """
    _id: int
    _name: str
    _builder: Builder[T]
    _validator: Validator[T]
    
    def __init__(self, id: int, name: str, builder: Builder[T], validator: Validator[T]):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   builder (Builder[T])
            *   validator (Validator[T])

        # Returns:
        None

        # Raises:
        None
        """
        super().__init__(id=id, name=name, certifier=validator)
        self._builder = builder
    
    #
    # @property
    # def id(self) -> int:
    #     """get entity id"""
    #     return self._id
    #
    # @property
    # def name(self) -> str:
    #     """get entity designation"""
    #     return self._name
    
    @property
    def entity_builder(self) -> Builder[T]:
        """get entity builder"""
        return self._builder
    
    @property
    def entity_validator(self) -> Validator[T]:
        """get entity validator"""
        return self.certifier
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, EntityService):
                return True
        return False


def __hash__(self):
    return hash(self._id)


def __str__(self):
    return f"id:{self._id}, designation:{self._name}"
