# src/logic/system/microservice/integrity/validator.py

"""
Module: logic.system.microservice.integrity.service
Author: Banji Lawal
Created: 2025-11-18
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from system import Microservice, Builder, Validator

T = TypeVar("T")


class IntegrityMicroservice(ABC, Microservice[Generic[T]]):
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
        schema: schema

    Provides:
        -   builder() -> Builder[T]
        -   validator() -> Validator[T]

    Super Class:
        Microservice
    """
    
    def __init__(self, id: int, name: str,):
        """
        Args:
            id: int
            name: str[T]
        """
        super().__init__(id=id, name=name,)
    
    @property
    @abstractmethod
    def builder(self) -> Builder[T]:
        pass
    
    @property
    @abstractmethod
    def validator(self) -> Validator[T]:
        pass
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, IntegrityMicroservice):
                return True
        return False

    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return f"id:{self._id}, schema:{self._name}"
