# src/operand/operand.py

"""
Module: operand.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""
from abc import abstractmethod
from typing import AnyStr


class Operand:
    """
    Role:
        -   Data Holder

    Responsibilities:
        1. Represent an item that has properties.

    Attributes:

    Provides:

    Super Class:
    """
    _a: Optional[Any]
    _b: Optional[Any]
    
    def __init__(self, a: Optional[Any] | None = None, b: Optional[b] | None = None,):
        """
        Args:
            a: Any
            b: Any
        """
        
    @property
    @abstractmethod
    def operand(self) -> Any:
        pass
    