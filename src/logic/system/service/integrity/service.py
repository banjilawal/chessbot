# src/logic/system/service/integrity/service.py

"""
Module: logic.system.service.integrity.service
Author: Banji Lawal
Created: 2025-11-18
"""

from abc import ABC
from typing import Generic, TypeVar

from logic.square.database.kernel.operation.collision.exception import id
from logic.system import Service, Builder, Validator

T = TypeVar("T")


class IntegrityService(ABC, Service[Generic[T]]):
    """
    Role:
        -   Microservice API
        -   Integrity Lifecycle Manager

    Responsibilities:
        1.  Mutates Model instances
        2.  Ensure Model integrity and consistency when its state changes.
        3.  Build Model instances that satisfy integrity contracts
        4.  Maintain the ModelIntegrity Lifecycle.

    Atrributes:
        id: int
        name: name
        builder: Builder[T]
        validator: Validator[T]

    Provides:

    Super Class:
        Service
    """
    _builder: Builder[T]
    _validator: Validator[T]
    
    def __init__(
            self,
            id: int,
            name: str,
            builder: Builder[T],
            validator: Validator[T]
    ):
        """
        Args:
            id: int
            name: str
            builder: Builder[T]
            validator: Validator[T]
        """
        super().__init__(id=id, name=name,)
        self._builder = builder
        self._validator = validator
    
    @property
    def builder(self) -> Builder[T]:
        return self._builder
    
    @property
    def validator(self) -> Validator[T]:
        return self.certifier
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, IntegrityService):
                return True
        return False

    def __hash__(self):
        return hash(self._id)
    
    def __str__(self):
        return f"id:{self._id}, name:{self._name}"
