# src/logic/system/service/integrity/compute.py

"""
Module: logic.system.service.integrity.service
Author: Banji Lawal
Created: 2025-11-18
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from logic.system import Service, BuildProcess, ValidationProcess

T = TypeVar("T")


class IntegrityService(ABC, Service[Generic[T]]):
    """
    Role:
        -   Microservice API
        -   Stateless Integrity Lifecycle Manager

    Responsibilities:
        1.  Mutates Model instances
        2.  Ensure Model integrity and consistency when its state changes.
        3.  Build Model instances that satisfy integrity contracts
        4.  Maintain the Model integrity lifecycle.

    Attributes:
        id: int
        name: name

    Provides:

    Super Class:
        Service
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
    def build(self) -> BuildProcess[T]:
        pass
    
    @property
    @abstractmethod
    def validation(self) -> ValidationProcess[T]:
        pass
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, IntegrityService):
                return True
        return False

    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return f"id:{self._id}, name:{self._name}"
