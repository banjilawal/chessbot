# src/operand/dto/operand.py

"""
Module: operand.dto.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from abc import abstractmethod

from typing import Generic, Optional, TypeVar

from blueprint import Blueprint
from operand import Operand

T = TypeVar("T")

class DtoOperand(Operand, Generic[T]):
    """
    Role:
        -   DTO

    Responsibilities:
        2.  Transports either an Object or its Blueprint.

    Attributes:
        entity: [T | Blueprint[T]]
        is_empty: bool
        has_overflow: bool
        is_model_operand: bool
        is_blueprint_operand: bool
        to_dict: Dict[str, Any]
        size: int

    Provides:
        -   extract_blueprint() -> Optional[Blueprint[T]]

    Super Class:
        Operand
    """

    @property
    @abstractmethod
    def entity(self) -> [T | Blueprint[T]]:
        pass
    
    @property
    @abstractmethod
    def is_model_operand(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def is_blueprint_operand(self) -> bool:
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
    
    @abstractmethod
    def extract_blueprint(self) -> Optional[Blueprint[T]]:
        pass

    