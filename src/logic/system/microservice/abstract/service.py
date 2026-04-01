# src/logic/system/microservice/abstract/validator.py

"""
Module: logic.system.microservice.abstract.service
Author: Banji Lawal
Created: 2025-11-18
"""

from abc import ABC
from typing import Generic, TypeVar

from logic.system import Validator

T = TypeVar("T")


class Microservice(ABC, Generic[T]):
    """
        -   API
        
    About Microservices:
        -   Stateless
        -   Pluggable
        -   Source of operations producing different Result types.
        -   Hosts workers that complete tasks for a stateful data-holder.
        

    Responsibilities:
        1.  Platform primitive to build Microservice APIs.
        
    Attributes:
        id: int
        name: str
        
    Provides:
    
    Super Class:
    """
    _id: int
    _name: str

    def __init__(self, id: int, name: str,):
        """
        Args:
            id: int
            name: str
        """
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
        if isinstance(other, Microservice):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return f"id:{self._id}, name:{self._name}"
