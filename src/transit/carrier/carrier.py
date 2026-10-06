# src/transit/carrier/carrier.py

"""
Module: transit.carrier.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from abc import ABC, abstractmethod

from typing import Generic, Optional, TypeVar

from domain import Blueprint

T = TypeVar("T")

class EntityCarrier(ABC, Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Object or its Blueprint.

    Attributes:
        model: Optional[T]
        blueprint: Optional[Blueprint[T]]
        size: int
        is_empty: bool
        has_model: bool
        has_blueprint: bool
        
        is_consistent: bool
        is_not_consistent: bool

    Provides:
        -   def extract_blueprint() -> Optional[Blueprint[T]]

    Super Class:
    """
    
    def __init__(
            self
    ):
        """
        Args:
            model: Optional[T]
            blueprint: Optional[Blueprint[T]]
        """


    @property
    def entity(self) -> Optional[T | Blueprint[T]]:
        if (
                self.is_empty or
                self.is_not_consistent
        ):
            return None
        if self._model is not None:
            return self._model
        return self._blueprint
    
    @property
    def has_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None
        )
    
    @property
    @abstractmethod
    def has_blueprint(self) -> bool:
        return (
                self._model is None and
                self._blueprint is not None
        )
    
    @property
    def size(self) -> int:
        return len([self._model, self._blueprint])
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_consistent(self) -> bool:
        return self.size == 1
    
    @property
    def is_not_consistent(self) -> bool:
        return self.size > 1
    
    @abstractmethod
    def extract_blueprint(self) -> Optional[Blueprint[T]]:
        pass

    