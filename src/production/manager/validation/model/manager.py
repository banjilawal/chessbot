# src/production/manager/validation/model/manager.py

"""
Module: production.manager.validation.model.manager
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar, cast

from artifcat import ValidationResult
from domain import Model
from production import ColliderManager, ModelColliderProducer
from transit import ModelCarrier, ModelColliderRouter
from util import LoggingLevelRouter

T = TypeVar("T", bound="Model")


class ModelColliderManager(ColliderManager[T], ABC, Generic[T]):
    """
    Role
        - Integrity, Consistency Maintenance

    Responsibilities:
        1.  Run integrity checks on an object or its blueprint encapsulated inside their
            EntityCarrier.
        2.  Makes sure objects or their blueprints are safe before they are used.
        3.  Pluggable validation module.

    Attributes:
        router: ModelColliderRouter[T]
        producer: ModelColliderProducer[T]

    Provides:
        -   def execute(item: Any) -> ValidationResult[ModelCarrier[T]]
    
    Super
        ColliderManager
    """
    
    def __init__(
            self, 
            producer: ModelColliderProducer[T],
            router: ModelColliderRouter[T],
    ):
        """
        Args:
            producer: ModelColliderProducer[T]
            router: ModelColliderRouter[T]
        """
        super().__init__(producer=producer, router=router)
     
    @property
    def producer(self) -> ModelColliderProducer[T]:
        return cast(ModelColliderProducer[T], super().producer)
        
    @property
    def router(self) -> ModelColliderRouter[T]:
        return cast(ModelColliderRouter[T], super().router)
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[ModelCarrier[T]]:
        """
        Verify the item is an EntityCarrier whose payload is safe.
        Args:
            item: Any
        Returns:
           ValidationResult[T]
        Raises:
            ValidatorException
        """
        pass
    
    
