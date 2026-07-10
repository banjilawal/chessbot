# src/operand/register/entity/operand.py

"""
Module: operand.register.entity.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, cast

from err import NullException
from operand import Operand, Register


class EntityRegister(Register[Any]):
    """
    Role:
        -   Operand
        -   Data Holder

    Responsibilities:
        1.  Contains the operand and null_exception for an entity.

    Attributes:
        operand: Operand
        null_exception: NullException
            
    Provoperandes:

    Super Class:
    """
    
    def __init__(self, operand: Any, null_exception: NullException,):
        """
        Args:
            operand: Operand
            null_exception: NullException
        """
        super().__init__(a=operand, b=null_exception)
        
    @property
    def operand(self) -> Any:
        return cast(Any, self.a)
    
    @property
    def null_exception(self) -> NullException:
        return cast(NullException, self.null_exception)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, EntityRegister):
            return (
                    self.operand == other.operand and
                    self.null_exception == other.null_exception
            )
    
