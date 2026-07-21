# src/carrier/operand.py

"""
Module: carrier.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""
from _ast import Dict
from abc import ABC, abstractmethod

from typing import Any, Generic, Optional, TypeVar

from blueprint import Blueprint
from toggle import Toggle

T = TypeVar("T")

class EntityCarrierToggle(ABC, Generic[T]):
    """
    Role:
        -   ENTITY

    Responsibilities:
        2.  Transports either an Object or its Blueprint.

    Attributes:
        is_model_operand: bool
        is_blueprint_operand: bool
        
        entity: [T | Blueprint[T]]
        is_empty: bool
        has_overflow: bool
        to_dict: Dict[str, Any]
        size: int

    Provides:
        -   extract_blueprint() -> Optional[Blueprint[T]]

    Super Class:
        Toggle
    """
    
    def __init__(self):
        super().__init__()

    @property
    @abstractmethod
    def entity(self) -> [T|Blueprint[T]]:
        pass
    
    @property
    @abstractmethod
    def is_model_carrier(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def is_blueprint_operand(self) -> bool:
        pass
    
    @abstractmethod
    def extract_blueprint(self) -> Optional[Blueprint[T]]:
        pass
    
    @property
    def no_active_toggles(self) -> bool:
        return self.active_toggles == 0
    
    @property
    def excess_toggles(self) -> bool:
        return self.active_toggles > 1
    
    @property
    def active_toggles(self) -> int:
        return len(self.to_dict)
    
    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass

    