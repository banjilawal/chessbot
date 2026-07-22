# src/toolkit/builder/model/model/model.model.py

"""
Module: toolkit.builder.model.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from model import Model

T = TypeVar("T", bound="Model")

class ModelModel(Model, Generic[T]):
    """
    Role:
        -   Dependency Management
        
    Responsibilities:
        1.  Contains a pair used in a binary operation whose operands must have
            the same type.
        
    Attributes:
        a: T
        b: T
        
    Provides:
    
    Super Class:
        Model
    """
    
    def __init__(self, a: T, b: T, id: Optional[int] | None= None,):
        """
        Args:
            a: T
            b: T
            id: Optional[int]
        """
        super().__init__(a=a, b=b, id=id)
        
        @property
        def a(self) -> T:
            return cast(T, super().a)
        
        @property
        def b(self) -> T:
            return cast(T, super().a)