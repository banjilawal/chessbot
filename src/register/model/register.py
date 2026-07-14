# src/register/model/register.model.py

"""
Module: register.register
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, TypeVar

from register import Register

T = TypeVar("T", bound="Model")

class ModelRegister(Register, Generic[T]):
    """
    Role:
        -   Addressing
        -   Data-Holder
  
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
    
    def __init__(self, a: T, b: T,):
        """
        Args:
            a: T
            b: T
        """
        super().__init__(a=a, b=b)