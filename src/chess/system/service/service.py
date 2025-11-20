# src/chess/system/service/service.py

"""
Module: chess.system.service.service
Author: Banji Lawal
Created: 2025-11-18
"""

from abc import ABC
from typing import Generic, TypeVar

T = TypeVar("T")


class Service(ABC, Generic[T]):
    """
    # ROLE: Service, Encapsulation, API layer.

    # RESPONSIBILITIES:
    1.  Provide a single interface/entry point for T objects and modules.
    2.  Masks implementation details and business logic making features easier to use.
    3.  Protects T objects from direct, unprotected access.
    4.  Public facing API.

    # PROVIDES:
    Service

    # ATTRIBUTES:
    None
        * id (int):     Globally unique identifier for the service.
        
        * name (str):   Name shared by all instance of the service. Default: "Service".
    """
    SERVICE_NAME = "service"
    _int: int
    _name: str
    
    def __init__(self, id: int, name: str = SERVICE_NAME) -> None:
        self._int = id
        self._name = name
        
    @property
    def id(self) -> int:
        return self._int
    
    @property
    def name(self) -> str:
        return self._name
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, Service):
            return self._int == other._int
        return False
    
    def __hash__(self):
        return hash(self._int)
    
    def __str__(self):
        return f"id:{self._id}, name:{self._name}"