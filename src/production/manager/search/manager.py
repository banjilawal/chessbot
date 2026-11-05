# src/production/manager/validation/manager.py

"""
Module: production.manager.validation.manager
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from artifcat import ValidationResult
from exchange import SearchRequest
from production import ColliderProducer
from transit import EntityCarrier, ColliderRouter
from util import LoggingLevelRouter

T = TypeVar("T", bound="SearchRequest")


class SearchManager(ABC, Generic[T]):
    """
    Role
        -   Search Management

    Responsibilities:
        1.  Coordinates

    Attributes:
        producer: ColliderProducer[T]
        router: ColliderRouter[T]

    Provides:
        -   def execute(candidate: Any) -> ValidationResult[EntityCarrier[T]]:
    Super
    """
    _producer: ColliderProducer[T]
    _router: ColliderRouter[T]
    
    def __init__(
            self,
            producer: ColliderProducer[T],
            router: ColliderRouter[T],
    ):
        """
        Args:
            producer: ColliderProducer[T]
            router: ValidationRouter[T]
        """
        super().__init__()
        self._producer = producer
        self._router = router
     
    @property
    def producer(self) -> ColliderProducer[T]:
        return self._producer
        
    @property
    def router(self) -> ColliderRouter[T]:
        return self._router
    
    @abstractmethod
    @LoggingLevelRouter.monitor
    def execute(self, item: Any) -> ValidationResult[EntityCarrier[T]]:
        """
        Verify the candidate is an EntityCarrier whose payload is safe.
        Args:
            item: Any
        Returns:
           ValidationResult[T]
        Raises:
            ValidatorException
        """
        pass
    
    
