# src/chess/system/service/base/service.py

"""
Module: chess.system.service.base.service
Author: Banji Lawal
Created: 2025-11-18
"""

from abc import ABC
from typing import Generic, TypeVar

from chess.system import Validator

T = TypeVar("T")


class Service(ABC, Generic[T]):
    """
    # ROLE: Service, Lifecycle Management, Encapsulation, API layer.

    # RESPONSIBILITIES:
    
    # PARENT:
    None

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   id (int)
        *   name (str)
        *   validator (Validator[T])

    # INHERITED ATTRIBUTES:
    None
    """
    _id: int
    _name: str
    _certifier: Validator[T]
    
    def __init__(self, id: int, name: str, certifier: Validator[T], ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (nt)
            *   name (str)
            *   certifier (Validator[T])

        # Returns:
        None

        # Raises:
        None
        """
        self._id = id
        self._name = name
        self._certifier = certifier
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def certifier(self) -> Validator[T]:
        return self._certifier
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Service):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return f"id:{self._id}, name:{self._name}"
