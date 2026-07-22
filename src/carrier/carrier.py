# src/carrier/operand.py

"""
Module: carrier.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


from abc import ABC, abstractmethod

from typing import Any, Dict, Generic, Optional, TypeVar

from blueprint import Blueprint


T = TypeVar("T")

class EntityCarrierToggle(ABC, Generic[T]):
    """
    Role:
        -   ENTITY

    Responsibilities:
        2.  Transports either an Object or its Blueprint.

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
    def is_carrying_model(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def is_carrying_blueprint(self) -> bool:
        pass
    
    @property
    def is_not_carrying_anything(self) -> bool:
        return self.active_toggles == 0
    
    @property
    def is_carrying_too_much(self) -> bool:
        return self.active_toggles > 1
    
    @property
    def active_toggles(self) -> int:
        return len(self.to_dict)
    
    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def extract_blueprint(self) -> Optional[Blueprint[T]]:
        pass

    