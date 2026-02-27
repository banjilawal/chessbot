# src/chess/system/service/abstract/service.py

"""
Module: chess.system.service.abstract.service
Author: Banji Lawal
Created: 2025-11-18
"""

from abc import ABC
from typing import Generic, TypeVar

from chess.system import Validator

T = TypeVar("T")


class AbstractService(ABC, Generic[T]):
    """
    # ROLE: AbstractService

    # RESPONSIBILITIES:
    1.  Platform primitive to build Microservice APIs.
    2.  A Microservice is
            *   A set of modules, methods that are related to a either a task or data object.
            *   Its modules produce different Result types

    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   name (name)

    # INHERITED ATTRIBUTES:
    None

    # CONSTRUCTOR PARAMETERS:)
        *   id (int)
        *   name (name)

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
    None
    """
    
    _id: int
    _name: str
    _validator: Validator[T]
    
    def __init__(self, id: int, name: str,):
        self._id = id
        self._name = name
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AbstractService):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return f"id:{self._id}, name:{self._name}"
