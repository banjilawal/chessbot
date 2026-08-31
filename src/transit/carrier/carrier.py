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
        1.  Transport a hydrated Object or its Blueprint across processing boundaries.

    Attributes:
        size: int
        
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [T | Blueprint[T]]


    Provides:
        - def extract_blueprint() -> Optional[Blueprint[T]]

    Super Class:
    """
    
    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def entity(self) -> Optional[T|Blueprint[T]]:
        pass
    
    @property
    @abstractmethod
    def is_carrying_model(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def is_carrying_blueprint(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def is_empty(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def size(self) -> int:
        pass
    
    @property
    @abstractmethod
    def is_over_capacity(self) -> bool:
        pass
    
    @abstractmethod
    def extract_blueprint(self) -> Optional[Blueprint[T]]:
        pass

    