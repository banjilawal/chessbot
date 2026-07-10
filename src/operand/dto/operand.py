# src/operand/dto/operand.py

"""
Module: operand.dto.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from abc import ABC, abstractmethod

from typing import Any, Generic, Optional, TypeVar

from blueprint import Blueprint

T = TypeVar("T", bound="Operand")

class DtoOperand(ABC, Generic[T]):
    """
    Role:
        -   Data Holder

    Responsibilities:
        1. Represent an item that has properties.

    Attributes:

    Provides:

    Super Class:
    """

        
    @property
    @abstractmethod
    def operand(self) -> [T|Blueprint[t]]:
        pass
    