# src/transit/carrier.py

"""
Module: transit.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from abc import ABC, abstractmethod

from typing import Generic, Optional, TypeVar

from fabrication.blueprint import Blueprint


T = TypeVar("T")

class EntityCarrier(ABC, Generic[T]):
    """
    Role:
        -   Data Transport

    Responsibilities:
        1.  Transport either:
            -   an Object
            -   an ObjectBlueprint

    Attributes:
        is_model_carrier: bool
        is_blueprint_carrier: bool
        
        entity: [T | Blueprint[T]]
        is_empty: bool
        has_overflow: bool
        to_dict: Dict[str, Any]
        size: int

    Provides:
        -   extract_blueprint() -> Optional[Blueprint[T]]

    Super Class:
    """
    
    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def entity(self) -> [T|Blueprint[T]]:
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
    def is_not_carrying_anything(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def is_carrying_too_much(self) -> bool:
        pass
    
    @abstractmethod
    def extract_blueprint(self) -> Optional[Blueprint[T]]:
        pass

    