# src/logic/system/microservice/integrity/validator.py

"""
Module: logic.system.microservice.integrity.service
Author: Banji Lawal
Created: 2025-11-18
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from logic.system import MicroService, Builder, Validator

T = TypeVar("T")


class IntegrityMicroService(ABC, MicroService[Generic[T]]):
    """
    Role:
        -   API
        -   Stateless microservice
        -   Lifecycle Manager
        -   Operations Provider

    Responsibilities:
        1.  Baremetal service request API.
        2.  Maintain the build-validation security lifecycle.

    Attributes:
        id: int
        name: name

    Provides:
        -   build() -> Builder[T]
        -   validation() -> Validator[T]

    Super Class:
        MicroService
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
    def validation(self) -> Validator[T]:
        pass
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, IntegrityMicroService):
                return True
        return False

    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return f"id:{self._id}, name:{self._name}"
