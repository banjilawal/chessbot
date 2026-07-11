# src/operand/operand.py

"""
Module: operand.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""
from abc import abstractmethod
from typing import Any, Dict


class Operand:
    """
    Role:
        -   Data Holder

    Responsibilities:
        1. Contains one of two types of entity.

    Attributes:
        entity: Any
        to_dict: Dict[str, Any]
        is_empty: bool
        has_overflow: bool
        size: int

    Provides:

    Super Class:
    """
        
    @property
    @abstractmethod
    def entity(self) -> Any:
        pass
    
    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass
    
    @property
    @abstractmethod
    def is_empty(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def has_overflow(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def size(self) -> int:
        pass
    