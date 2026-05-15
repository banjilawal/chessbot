# src/microservice/microservice.py

"""
Module: microservice.microservice
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from operation import Validator
from pipeline import BuildPipeline

T = TypeVar("T")


class Microservice(ABC, Generic[T]):
    """
    Role:
        -   API
        -   Lifecycle Manager
        -   Operations Provider
        -   Stateless Microservice
        
    About:
        Avoids casting an entity's builders and validators by making them abstract
        properties.

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the build-validation security lifecycle.

    Attributes:
        id: int
        name: str

    Provides:
        -   builder() -> Builder[T]
        -   validator() -> Validator[T]

    Super Class:
        Microservice
    """
    NAME = "microservice"
    _id: int
    _name: str
    
    def __init__(self, id: int, name: str,):
        """
        Args:
            id: int
            name: str[T]
        """
        self._id = id
        self._name = self.NAME
        
    
    @property
    @abstractmethod
    def builder(self) -> BuildPipeline[T]:
        pass
    
    @property
    @abstractmethod
    def validator(self) -> Validator[T]:
        pass
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, Microservice):
                return True
        return False

    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return f"id:{self._id}, name:{self._name}"
